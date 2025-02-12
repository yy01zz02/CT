from flask import Flask, request
import subprocess
import ipaddress
import re

app = Flask(__name__)

def is_valid_input(url):
    try:
        ipaddress.ip_address(url)
        return True
    except ValueError:
        if re.fullmatch(r'^[a-zA-Z0-9.-]+\Z', url):
            return True
        return False

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url or not is_valid_input(url):
        return "Invalid URL", 400
    
    try:
        output = subprocess.check_output(
            ['/bin/ping', '-c', '1', url],
            stderr=subprocess.STDOUT,
            text=True,
            timeout=10
        )
    except subprocess.CalledProcessError as e:
        output = e.output
    except subprocess.TimeoutExpired:
        return "Request timed out", 504
    
    return output