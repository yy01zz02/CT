from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url or not re.match(r'^[a-zA-Z0-9.-]+$', url):
        return "Invalid URL", 400
    
    try:
        output = subprocess.check_output(["/bin/ping", "-c", "3", url], stderr=subprocess.STDOUT, timeout=5, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    except Exception as e:
        return str(e), 500
    
    return output
