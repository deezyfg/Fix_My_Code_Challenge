#!/usr/bin/python3
"""
Simple Web Server

This script sets up a basic Flask web server to handle API requests.
"""

from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """
    Error Handler for 404

    This function handles 404 errors by returning a JSON response.
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # Command to start the server: python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
