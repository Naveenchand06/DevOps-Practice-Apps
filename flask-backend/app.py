from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # 👈 enables CORS on all routes


@app.route("/healthz")
def healthz():
    return "OK"


@app.route("/data1")
def data1():
    return jsonify({
        "id": random.randint(1, 100),
        "name": "Random Data 1"
    })


@app.route("/data2")
def data2():
    return jsonify({
        "timestamp": random.random(),
        "status": "Generated from Flask"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
