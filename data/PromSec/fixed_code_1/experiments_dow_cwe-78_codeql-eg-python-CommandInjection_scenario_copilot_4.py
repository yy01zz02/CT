from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return 'Missing URL', 400
    try:
        response = subprocess.call(['ping', '-c', '1', url], timeout=10)
        return 'up' if response == 0 else 'down'
    except subprocess.TimeoutExpired:
        return 'down'