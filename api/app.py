"""
Tiny Flask app exposing the pipeline as an HTTP endpoint.
Run with: python -m api.app
"""

from flask import Flask, jsonify

from src.fetcher import fetch_data
from src.processor import process_data
from utils.logger import logger

app = Flask(__name__)


@app.route("/report")
def report():
    logger.info("Handling /report request")
    raw = fetch_data()
    processed = process_data(raw)
    summary = processed["summary"]
    return jsonify(summary.to_dict(orient="records") if summary is not None else [])


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
