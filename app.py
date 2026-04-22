from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is alive 🚀"

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
