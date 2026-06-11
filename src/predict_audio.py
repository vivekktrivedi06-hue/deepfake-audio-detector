import joblib
import numpy as np
from feature_extraction import extract_features

# Load model
model = joblib.load("models/deepfake_model.pkl")

def predict_audio(file_path):
    features = extract_features(file_path)

    if features is None:
        return "Error"

    features = features.reshape(1, -1)

    prediction = model.predict(features)[0]

    if prediction == 1:
        return "FAKE"
    else:
        return "REAL"


if __name__ == "__main__":
    file_path = "dataset/archive-5/DEMONSTRATION/DEMONSTRATION/linus-to-musk-DEMO.mp3"
    result = predict_audio(file_path)
    print("Prediction:", result)