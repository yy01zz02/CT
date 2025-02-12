from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    try:
        subprocess.run(['ping', '-c', '1', url], check=True, timeout=5, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        return f"The URL {url} is alive"
    except subprocess.CalledProcessError:
        return f"The URL {url} is not alive"
    except subprocess.TimeoutExpired:
        return f"Ping request timed out for URL {url}"