from flask import Flask, request
import subprocess  # nosec B404
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    if not re.fullmatch(r'^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$', url):
        return "Invalid URL", 400
    output = subprocess.run(  # nosec B603
        ["/usr/bin/ping", "-c", "1", "--", url],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False
    ).stdout
    return output