from flask import Flask, request
import re
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url:
        if not re.fullmatch(r'^[a-zA-Z0-9.:-]+$', url) or url.startswith('-'):
            return "Invalid URL", 400
        response = subprocess.run(['ping', '-c', '1', '-W', '2', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return str(response.returncode)
    return "URL parameter is missing", 400