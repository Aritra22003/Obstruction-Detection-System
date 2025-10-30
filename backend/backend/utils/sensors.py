# utils/sensors.py
# small helper functions for sensor value validation / normalization

def clamp(v, minv, maxv):
    try:
        v = float(v)
    except:
        return minv
    return max(minv, min(maxv, v))

def normalize_sample(sample):
    return {
        "distance_cm": clamp(sample.get("distance_cm", 0), 0, 10000),
        "lidar_intensity": clamp(sample.get("lidar_intensity", 0), 0.0, 1.0),
        "camera_confidence": clamp(sample.get("camera_confidence", 0), 0.0, 1.0),
        "ir_temp_diff": clamp(sample.get("ir_temp_diff", 0), 0.0, 100.0),
        "sonar_echo": clamp(sample.get("sonar_echo", 0), 0.0, 1.0),
    }
