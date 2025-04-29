import requests

url = "http://127.0.0.1:5000/predict"
data = {"features": [5.1, 3.5, 1.4, 0.2]}  # Example features
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Prediction:", response.json())
