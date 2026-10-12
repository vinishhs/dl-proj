import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_emotion

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio = request.files["audio"]
    temp_path = "temp_audio.wav"
    audio.save(temp_path)

    try:
        result = predict_emotion(temp_path)
        return jsonify(result)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    app.run(debug=True)
