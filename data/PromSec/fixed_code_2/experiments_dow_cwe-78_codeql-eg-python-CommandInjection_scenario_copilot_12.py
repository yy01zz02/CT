from flask import Flask, request
import os
import sys
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return 'URL parameter is missing', 400
    # Validate URL format to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.:-]+$', url):
        return 'Invalid URL format', 400
    cmd = ['ping', '-c', '1', url]
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=10, text=True)
        rv = result.returncode
    except subprocess.TimeoutExpired:
        return f'{url} is not alive (timeout)'
    if rv == 0:
        return f'{url} is ALIVE'
    else:
        return f'{url} is not alive'