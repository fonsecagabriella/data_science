FROM agrigorev/zoomcamp-model:2025

# Work inside /app (this is where the base image usually lives too)
WORKDIR /app

# Copy everything from your project into the image:
# - pyproject.toml  (dependency list)
# - predict.py      (FastAPI app)
# - anything else your app needs
COPY . .

# Install all dependencies defined in pyproject.toml.
# pip will read pyproject.toml and install your project + its deps.
RUN pip install --no-cache-dir scikit-learn==1.6.1 fastapi "uvicorn[standard]"

# Expose the port your FastAPI app uses
EXPOSE 9696

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
