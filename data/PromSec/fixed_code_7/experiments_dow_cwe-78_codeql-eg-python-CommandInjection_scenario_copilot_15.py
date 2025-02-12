from flask import Flask, request
import re
import subprocess  # nosec B404

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url:
        if not re.fullmatch(r'^[a-zA-Z0-9.:-]+$', url) or url.startswith('-'):
            return "Invalid URL", 400
        response = subprocess.run(['/bin/ping', '-c', '1', '-W', '2', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # nosec B603
        return str(response.returncode)
    return "URL parameter is missing", 400
