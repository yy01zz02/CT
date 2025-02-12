from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url:
        if not re.fullmatch(r'^[a-zA-Z0-9.:-]+$', url) or url.startswith('-'):
            return "Invalid URL", 400
        response = os.system(f"ping -c 1 -W 2 {url} > /dev/null 2>&1")
        return str(response >> 8)
    return "URL parameter is missing", 400