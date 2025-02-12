from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is required.", 400

    if not re.match(r'^[a-zA-Z0-9.:-]+$', url) or url.startswith('-'):
        return "Invalid URL format.", 400

    try:
        output = subprocess.check_output(['/usr/bin/ping', '-c', '4', url])
    except subprocess.CalledProcessError as e:
        output = e.output

    return output