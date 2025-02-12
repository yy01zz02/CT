from flask import Flask, request
import subprocess  # nosec: B404
import re
import ipaddress

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is required.", 400

    url = url.split()[0]
    if url.startswith('-'):
        return "Invalid URL format.", 400

    try:
        ipaddress.ip_address(url)
    except ValueError:
        if not re.fullmatch(r'^([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$', url):
            return "Invalid URL format.", 400

    try:
        output = subprocess.check_output(['/usr/bin/ping', '-c', '4', url])  # nosec: B603
    except subprocess.CalledProcessError as e:
        output = e.output

    return output