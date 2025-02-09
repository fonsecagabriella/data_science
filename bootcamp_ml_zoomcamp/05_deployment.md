# Deployment

- **Train and Save the Model:** After training the model, save it as a file, to use it for making predictions in future.
- **Create API Endpoints:** Make the API endpoints in order to request predictions. It is possible to use the Flask framework to create web service API endpoints that other services can interact with.
- **Some other server deployment options**
    -- **Pipenv:** Create isolated environments to manage the Python dependencies of the web service, ensuring they don’t interfere with other services on the machine.
    -- **Docker:** Package the service in a Docker container, which includes both system and Python dependencies, making it easier to deploy consistently across different environments.
- **Deploy to the Cloud:** Finally, deploy the Docker container to a cloud service like AWS to make the model accessible globally, ensuring scalability and reliability.


## 1.0 Saving and Loading the Model

- After you trained the model in your jupiter notebook, `import pickle` to save the model.
- Download your jupiter notebook as `python .py`, and format it a little bit, remove what you don't need
- The file you downloaded is your python script you can usewgwt


## 2.0 Web Service  

**Web service**:  A service that communicates via a network. You send a request (ping), get a treated output (pong)
 
- Here we create a `Flask Web Service`, named `ping.py` in the `code_deployment` folder. 
- `curl` requests a webservice

````
curl http://0.0.0.0:9696/ping
````

## 3.0 Serving the churn model with Flask
<img src="/imgs/serving-flask.png" width="70%">

## 4.0 Pipenv

- Install pipenv
- pipenv shell
- pipenv run gunicorn --bind 0.0.0.0:9696 predict:app