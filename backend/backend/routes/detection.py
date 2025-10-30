from flask import Blueprint, request, jsonify
import joblib, os
import numpy as np

detection_bp = Blueprint("detection_bp", __name__)

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model", "knn.pkl")
SCALER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "processed", "scaler.pkl")

# lazy-load models
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    model = None
    scaler = None

@detection_bp.route("/predict", methods=["POST"])
def predict():
    global model, scaler
    if model is None or scaler is None:
        return jsonify({"error": "Model or scaler not available on server."}), 500
    try:
        data = request.get_json()
        features = [
            float(data.get("distance_cm", 0)),
            float(data.get("lidar_intensity", 0)),
            float(data.get("camera_confidence", 0)),
            float(data.get("ir_temp_diff", 0)),
            float(data.get("sonar_echo", 0)),
            float(data.get("lidar_intensity", 0)) / (float(data.get("camera_confidence", 0)) + 1e-6)
        ]

        scaled = scaler.transform([features])
        pred = int(model.predict(scaled)[0])
        status = "OBSTRUCTION DETECTED" if pred == 1 else "CLEAR PATH"
        prob = None
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(scaled)[0].max()
        return jsonify({"prediction": status, "probability": float(prob) if prob is not None else None})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
