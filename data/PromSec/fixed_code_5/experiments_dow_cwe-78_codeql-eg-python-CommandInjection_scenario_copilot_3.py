from flask import Flask, request
import re
from pythonping import ping

app = Flask(__name__)

@app.route('/url/ping')
def ping_route():
    url = request.args.get('url')
    if not url:
        return '<h1>URL parameter is missing</h1>', 400
    if not re.fullmatch(r'^[a-zA-Z0-9.-:]+$', url):
        return '<h1>Invalid URL format</h1>', 400
    try:
        result = ping(url, count=1, timeout=2)
        if result.success():
            return f'<h1>{url} is alive</h1>'
        else:
            return f'<h1>{url} is not alive</h1>'
    except Exception:
        return f'<h1>{url} is not alive</h1>'