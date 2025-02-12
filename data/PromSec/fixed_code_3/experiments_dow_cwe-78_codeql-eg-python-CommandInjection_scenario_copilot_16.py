from flask import Flask, request
import json
import re
import socket

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return json.dumps({"error": "Missing URL parameter"}), 400
    
    if not re.fullmatch(r'^[a-zA-Z0-9\.\-:]+$', url):
        return json.dumps({"error": "Invalid URL format"}), 400

    try:
        host = url.split(':')[0]
        socket.create_connection((host, 80), timeout=5)
        alive = 1
    except (socket.timeout, socket.error, OSError, ValueError):
        alive = 0
    
    return json.dumps({'alive': alive})