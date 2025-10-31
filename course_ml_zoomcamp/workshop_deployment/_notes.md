# Workshop - How to deploy ML models with FastAPI, Docker and Fly.io

[Link to the video](https://www.youtube.com/watch?v=jzGzw98Eikk)

FastAPI is a modern Python framework for building web services and APIs. FastAPI is preferred over Flask because it provides automatic data validation, interactive API documentation, and better support for asynchronous programming.

`pip install fastapi uvicorn`

- FastAPI is the framework.
- Uvicorn is an ASGI server, used to run FastAPI applications.

## 01. Creating a Simple FastAPI Application
Create a Python script, for example, `ping.py`. Begin by importing FastAPI and initializing the application:

```python 
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return "pong"

```

This defines a basic endpoint /ping that responds with "pong".

Run the app using Uvicorn:
`uvicorn ping:app --host 127.0.0.1 --port 9696 --reload`

- `--reload` enables auto-reloading on code changes during development.

- Access `http://127.0.0.1:9696/ping` in the browser to see the response.

- Or send a request via the terminal `curl localhost:9696/ping`

- You can run `localhost:9696/docs` to check all the apps you have

## 02. Creating a Prediction Endpoint
Next, integrate the machine learning model prediction logic into the FastAPI app.

Define a POST endpoint /predict that accepts customer data and returns churn probability.
Example skeleton:

```python
from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.post("/predict")
def predict(customer: Dict):
    # Convert input dictionary to model features
    # Apply the pipeline model to predict churn probability
    churn_proba = model.predict_proba([customer])[0, 1]
    churn = churn_proba >= 0.5
    return {"churn_probability": churn_proba, "churn": churn}

```

Here, customer is expected as a JSON dictionary.
The model should be pre-loaded from a saved pickle file.

##  03. Typing and Input Validation with Pydantic
FastAPI leverages Pydantic for data validation. Define a Pydantic model representing the expected input schema:

``` python
from pydantic import BaseModel
from typing import Literal, Optional

class Customer(BaseModel):
    gender: Literal["Male", "Female"]
    senior_citizen: int  # 0 or 1
    partner: Literal["Yes", "No"]
    dependents: Literal["Yes", "No"]
    tenure: int
    phone_service: Literal["Yes", "No"]
    # Add all other expected fields here with types and constraints

@app.post("/predict")
def predict(customer: Customer):
    customer_dict = customer.dict()
    churn_proba = model.predict_proba([customer_dict])[0, 1]
    churn = churn_proba >= 0.5
    return {"churn_probability": churn_proba, "churn": churn}

```

This ensures that incoming requests must conform to the specified schema.
Invalid requests will automatically receive proper error responses.

## 04. Loading the Model
Load the trained pipeline (which includes preprocessing and the logistic regression model) once at startup:

```py
import pickle

with open("model.bin", "rb") as f_in:
    model = pickle.load(f_in)
```

Place this at the top level in `predict.py` so it loads when the app starts.

## 05. Testing the API
FastAPI automatically generates interactive API docs at /docs (Swagger UI) and /redoc.
You can use the Swagger UI to test the /predict endpoint by sending JSON payloads.

Alternatively, use curl or Python requests library to send POST requests with JSON data.

Example using requests:

```python
import requests

url = "http://localhost:9696/predict"
customer_data = {
    "gender": "Male",
    "senior_citizen": 0,
    "partner": "No",
    "dependents": "No",
    "tenure": 6,
    "phone_service": "Yes",
    # other features...
}

response = requests.post(url, json=customer_data)
print(response.json())
```

## 06. Using uv for Dependency Management
- Install `uv` (a fast Python dependency manager) for managing virtual environments and dependencies:

```bash
pip install uv
uv init
uv add fastapi uvicorn scikit-learn pandas
```

This creates `pyproject.toml` and lock files to pin dependencies.

Run the app inside the uv virtual environment:
`uv run uvicorn predict:app --reload`

## 07. Containerizing with Docker
Create a Dockerfile for containerizing the FastAPI app:

```dockerfile
FROM python:3.12.1-slim-bookworm

WORKDIR /app

COPY pyproject.toml uv.lock /app/
RUN pip install uv && uv sync --no-dev

COPY predict.py model.bin /app/

EXPOSE 9696

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
```

Build and run the Docker container:

```bash
docker build -t churn-prediction .
docker run -p 9696:9696 churn-prediction
```

## 08. Deploying the Container
Use `fly.io` to deploy the containerized app:

- Install fly CLI and authenticate.
- Initialize fly app and deploy:

```bash
fly launch
fly deploy
```

The deployed app gets a public URL.
Update your marketing client script to send requests to the deployed URL.