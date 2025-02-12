from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400

    try:
        output = subprocess.check_output(
            ['/usr/bin/ping', '-c', '1', '--', url],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
    except subprocess.CalledProcessError:
        return f"Unable to ping {url}"

    if '1 received' in output:
        return f"{url} is alive"
    else:
        return f"Unable to ping {url}"