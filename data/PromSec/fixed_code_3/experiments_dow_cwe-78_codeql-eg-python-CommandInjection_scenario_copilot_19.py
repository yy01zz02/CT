from flask import Flask, request
import subprocess  # noqa: B404
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    
    if not re.fullmatch(r'^[a-zA-Z0-9.\-:]+$', url):
        return "Invalid URL format", 400
    
    result = subprocess.run(  # nosec B603
        ['/usr/bin/ping', '-c', '1', '--', url],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return f"{url} is up! - COPILOT" if result.returncode == 0 else f"{url} is down! - COPILOT"