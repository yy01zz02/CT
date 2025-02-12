from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

VALID_HOSTNAME_REGEX = re.compile(
    r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]))*$'
)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url or len(url) > 253 or not VALID_HOSTNAME_REGEX.match(url):
        return 'not ok'
    try:
        rv = subprocess.run(
            ['/usr/bin/ping', '-c', '1', url],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )
        return 'ok' if rv.returncode == 0 else 'not ok'
    except subprocess.TimeoutExpired:
        return 'not ok'