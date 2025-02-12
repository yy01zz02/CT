from flask import Flask, request
import re
import socket

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return 'URL parameter is missing', 400
    if not re.fullmatch(r'^[a-zA-Z0-9.-]+$', url) and not re.fullmatch(r'^[0-9.]+$', url):
        return 'Invalid URL format', 400
    try:
        socket.create_connection((url, 80), timeout=10)
        return f'{url} is ALIVE'
    except (socket.timeout, OSError):
        return f'{url} is not alive'
    except Exception as e:
        return f'Error checking {url}: {str(e)}', 500