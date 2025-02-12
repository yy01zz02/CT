from flask import Flask, request
import os
import shlex

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return '<h1>URL parameter is missing</h1>', 400
    safe_url = shlex.quote(url)
    pong = os.system(f"ping -c 1 {safe_url}")
    if pong == 0:
        return f'<h1>{url} is alive</h1>'
    else:
        return f'<h1>{url} is not alive</h1>'