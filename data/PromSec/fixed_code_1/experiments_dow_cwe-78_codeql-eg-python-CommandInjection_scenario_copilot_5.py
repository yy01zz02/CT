from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url or not re.match(r'^[a-zA-Z0-9.:-]+$', url):
        return "Invalid URL", 400
    cmd = ['ping', '-c1', url]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output