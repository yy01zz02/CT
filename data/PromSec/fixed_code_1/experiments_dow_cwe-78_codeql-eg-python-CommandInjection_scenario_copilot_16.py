from flask import Flask, request
import os
import json
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    command = ['ping', '-c', '1', url]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    data = {'alive': 1 if result == 0 else 0}
    return json.dumps(data)