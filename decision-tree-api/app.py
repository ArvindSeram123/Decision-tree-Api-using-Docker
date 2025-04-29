from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Decision Tree API!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = data["features"]  # Expecting a list of features
        prediction = model.predict([features])
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
