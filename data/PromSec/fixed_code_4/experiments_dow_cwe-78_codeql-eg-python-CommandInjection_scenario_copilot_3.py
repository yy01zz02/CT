from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return '<h1>URL parameter is missing</h1>', 400
    if not re.fullmatch(r'^[a-zA-Z0-9.-:]+$', url):
        return '<h1>Invalid URL format</h1>', 400
    result = subprocess.run(["/bin/ping", "-c", "1", "--", url], capture_output=True)  # nosec B603
    if result.returncode == 0:
        return f'<h1>{url} is alive</h1>'
    else:
        return f'<h1>{url} is not alive</h1>'
