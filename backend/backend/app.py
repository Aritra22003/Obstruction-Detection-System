from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from routes.detection import detection_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(detection_bp, url_prefix="/api")

@app.route("/")
def home():
    return jsonify({"message": "Obstruction Detection Backend Active"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
