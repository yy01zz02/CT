from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url:
        result = subprocess.run(['ping', url], capture_output=True, text=True)
        return str(result.returncode)
    return "URL parameter is missing", 400