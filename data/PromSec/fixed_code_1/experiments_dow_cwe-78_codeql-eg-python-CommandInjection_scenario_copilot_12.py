from flask import Flask, request, redirect
import os
import sys
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return 'URL parameter is missing', 400
    cmd = ['ping', '-c', '1', url]
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=10)
        rv = result.returncode
    except subprocess.TimeoutExpired:
        return '%s is not alive (timeout)' % url
    if rv == 0:
        return '%s is ALIVE' % url
    else:
        return '%s is not alive' % url