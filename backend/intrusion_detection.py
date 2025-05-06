import pickle
import numpy as np

with open("models/intrusion_model.pkl", 'rb') as f:
    model = pickle.load(f)

def detect_intrusion(packet_features):
    features = np.array(packet_features).reshape(1, -1)
    prediction = model.predict(features)
    return "Intrusion Detected!" if prediction == 1 else "Normal Traffic"

# def detect_intrusion(packet_features):
#     if len(packet_features) != 6:
#         return "Invalid input: expected 6 features"
#     features = np.array(packet_features).reshape(1, -1)
#     prediction = model.predict(features)
#     return "Intrusion Detected!" if prediction[0] == 1 else "Normal Traffic"
