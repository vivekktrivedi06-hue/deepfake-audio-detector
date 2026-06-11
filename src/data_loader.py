import os
import numpy as np
from feature_extraction import extract_features

def load_dataset(dataset_path):
    X = []
    y = []

    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)

                features = extract_features(file_path)

                if features is not None:
                    X.append(features)

                    # Label logic
                    if "fake" in root.lower():
                        y.append(1)
                    else:
                        y.append(0)

    return np.array(X), np.array(y)


if __name__ == "__main__":
    dataset_path = "dataset"
    X, y = load_dataset(dataset_path)

    print("Features shape:", X.shape)
    print("Labels shape:", y.shape)