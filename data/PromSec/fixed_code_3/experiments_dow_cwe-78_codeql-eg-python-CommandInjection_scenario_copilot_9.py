from flask import Flask, request
import subprocess  # nosec: B404
import socket
import re

app = Flask(__name__)

def is_valid_ip(ip_str):
    try:
        socket.inet_pton(socket.AF_INET, ip_str)
        return True
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, ip_str)
            return True
        except socket.error:
            return False

def is_valid_hostname(hostname):
    if len(hostname) > 253:
        return False
    allowed = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*$")
    return allowed.match(hostname) is not None

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400
    if not (is_valid_ip(url) or is_valid_hostname(url)):
        return "Invalid URL", 400

    try:
        output = subprocess.check_output(  # nosec: B603
            ['/usr/bin/ping', '-c', '1', '--', url],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
    except subprocess.CalledProcessError:
        return f"Unable to ping {url}"

    if '1 received' in output:
        return f"{url} is alive"
    else:
        return f"Unable to ping {url}"