from flask import Flask, request
import re
import ping3

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    
    if not re.fullmatch(r'^[a-zA-Z0-9.\-:]+$', url):
        return "Invalid URL format", 400
    
    is_up = ping3.ping(url, timeout=1, unit='ms') not in (None, False)
    return f"{url} is up! - COPILOT" if is_up else f"{url} is down! - COPILOT"