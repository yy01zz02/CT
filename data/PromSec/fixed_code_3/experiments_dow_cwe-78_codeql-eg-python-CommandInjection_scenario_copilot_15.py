from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url:
        if not re.fullmatch(r'^[a-zA-Z0-9.:-]+$', url) or url.startswith('-'):
            return "Invalid URL", 400
        result = subprocess.run(['/bin/ping', '--', url], capture_output=True, text=True)
        return str(result.returncode)
    return "URL parameter is missing", 400