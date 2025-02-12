from flask import Flask, request
import subprocess  # nosec
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return 'Missing URL', 400
    if not re.match(r'^[a-zA-Z0-9.:][a-zA-Z0-9.:-]*$', url):
        return 'Invalid URL', 400
    try:
        response = subprocess.call(['/bin/ping', '-c', '1', url], timeout=10)  # nosec
        return 'up' if response == 0 else 'down'
    except subprocess.TimeoutExpired:
        return 'down'