from flask import Flask, request
import subprocess  # nosec
import ipaddress
import re

app = Flask(__name__)

def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if not re.match(r'^[a-zA-Z0-9.-]+$', hostname):
        return False
    parts = hostname.split('.')
    for part in parts:
        if len(part) == 0 or len(part) > 63:
            return False
        if not re.match(r'^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$', part):
            return False
    return True

def validate_url(url):
    try:
        ipaddress.ip_address(url)
        return True
    except ValueError:
        return is_valid_hostname(url)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    if not validate_url(url):
        return "Invalid URL format", 400
    try:
        subprocess.run(  # nosec
            ['/usr/bin/ping', '-c', '1', url],
            check=True, timeout=5,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL
        )
        return f"The URL {url} is alive"
    except subprocess.CalledProcessError:
        return f"The URL {url} is not alive"
    except subprocess.TimeoutExpired:
        return f"Ping request timed out for URL {url}"