# Decision-tree-Api-using-Docker
A simple machine learning API using Flask + Docker to serve a Decision Tree model trained on sample data.
# This portfolio demonstrates end-to-end Machine Learning workflows containerized with Docker.

## 🔧 Projects

### 1. 📦 Model API (Flask)
- Serve a scikit-learn model
- Predict via POST `/predict`
- Built with: Flask, Docker

### 2. 🏋️‍♂️ Train Model in Docker
- Train a DecisionTreeClassifier inside Docker
- Save model artifacts to a volume

## 🚀 Tools
- Docker
- Python 3.9
- Flask
- scikit-learn

##✅ Running the model trainer inside Docker 
```bash
docker build -t model-trainer .
docker run -v "${PWD}/model_output:/app/model_output" model-trainer
```
and saved the model.pkl sucessfully ✅
Copy the tranied model inside decision-tree-api/ folder

##🔨  Lastly Build and Run the api using Docker
```bash
docker build -t decision-tree-api .
docker run -p 5000:5000 decision-tree-api
```

## Test the API using curl
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {"features": [5.1, 3.5, 1.4, 0.2]}  # Example features
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Prediction:", response.json())
```
