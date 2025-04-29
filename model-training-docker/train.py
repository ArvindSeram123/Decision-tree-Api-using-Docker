from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

# Load data
X, y = load_iris(return_X_y=True)

# Train model
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Save model to /app/model_output
os.makedirs("model_output", exist_ok=True)
with open("model_output/model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("✅ Model trained and saved!")
