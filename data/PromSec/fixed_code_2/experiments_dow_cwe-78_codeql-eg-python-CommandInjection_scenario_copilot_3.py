from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return '<h1>URL parameter is missing</h1>', 400
    result = subprocess.run(["ping", "-c", "1", url], capture_output=True)
    if result.returncode == 0:
        return f'<h1>{url} is alive</h1>'
    else:
        return f'<h1>{url} is not alive</h1>'