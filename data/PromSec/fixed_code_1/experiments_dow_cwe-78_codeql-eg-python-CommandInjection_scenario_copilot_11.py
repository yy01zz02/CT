from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    result = subprocess.run(['ping', '-c', '5', url], capture_output=True, text=True).returncode
    return "OK" if result == 0 else str(result)