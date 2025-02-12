from flask import Flask, request, redirect
import subprocess
import os
import re
import tempfile

app = Flask(__name__)

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9](?:[a-zA-Z0-9.-]*[a-zA-Z0-9])?$', host) is not None

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url or not is_valid_host(url):
        return "<h1>Invalid URL</h1>", 400

    ping_path = '/bin/ping'
    if not os.path.isfile(ping_path):
        return "<h1>Server Error</h1>", 500

    try:
        proc = subprocess.Popen([ping_path, '-c', '4', url],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, _ = proc.communicate()
    except Exception:
        return "<h1>Ping Failed</h1>", 500

    try:
        with tempfile.NamedTemporaryFile(mode='wb', delete=False) as tmpfile:
            tmpfile.write(stdout)
    except IOError:
        return "<h1>Output Error</h1>", 500

    return redirect(url) if proc.returncode == 0 else f"<h1>Can't ping {url}</h1>"