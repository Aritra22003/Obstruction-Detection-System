# Backend - Obstruction Detection System

Flask backend that exposes a `/api/predict` endpoint. It expects a POST JSON body with the following keys:
- distance_cm
- lidar_intensity
- camera_confidence
- ir_temp_diff
- sonar_echo

It returns JSON with `prediction` and optional `probability`.
