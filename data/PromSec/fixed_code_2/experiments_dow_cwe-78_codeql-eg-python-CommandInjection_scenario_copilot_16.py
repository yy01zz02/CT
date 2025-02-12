from flask import Flask, request
import json
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return json.dumps({"error": "Missing URL parameter"}), 400
    
    if not re.fullmatch(r'^[a-zA-Z0-9\.\-:]+$', url):
        return json.dumps({"error": "Invalid URL format"}), 400
    
    command = ['ping', '-c', '1', url]
    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        alive = 1 if result.returncode == 0 else 0
    except subprocess.TimeoutExpired:
        alive = 0
    
    return json.dumps({'alive': alive})