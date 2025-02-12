from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return 'not ok'
    try:
        rv = subprocess.run(['ping', '-c', '1', url], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return 'ok' if rv.returncode == 0 else 'not ok'
    except subprocess.TimeoutExpired:
        return 'not ok'