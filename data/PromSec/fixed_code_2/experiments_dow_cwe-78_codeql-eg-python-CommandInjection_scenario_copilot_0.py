from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    if not re.match(r'^[a-zA-Z0-9.-]+$', url):
        return "Invalid URL", 400
    output = subprocess.run(
        ["/usr/bin/ping", "-c", "1", "--", url],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
        shell=False
    ).stdout
    return output
