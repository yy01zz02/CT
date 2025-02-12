from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    cmd = ['ping', '-c', '1', '-t', '1', url]
    try:
        response = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        if response.returncode == 0:
            return f"The host {url} is UP."
        else:
            return f"The host {url} is DOWN."
    except subprocess.TimeoutExpired:
        return f"The host {url} is DOWN (timeout)."