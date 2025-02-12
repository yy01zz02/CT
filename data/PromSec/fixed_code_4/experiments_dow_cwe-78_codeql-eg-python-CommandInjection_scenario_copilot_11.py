from flask import Flask, request
import subprocess  # nosec B404
import re

app = Flask(__name__)

ALLOWED_HOSTNAME_PATTERN = re.compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9.-]*[a-zA-Z0-9])?$')

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url or not ALLOWED_HOSTNAME_PATTERN.match(url):
        return "Invalid URL", 400
    
    try:
        result = subprocess.run(['/bin/ping', '-c', '5', url],  # nosec B603
                               capture_output=True, text=True, check=True)
        return "OK"
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}", 500
