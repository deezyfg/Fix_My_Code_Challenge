#!/usr/bin/python3
"""
Index View

This script defines an endpoint to retrieve the status of the web server.
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Status Endpoint

    This function returns the status of the web server in JSON format.
    """
    return jsonify({"status": "OK"})
