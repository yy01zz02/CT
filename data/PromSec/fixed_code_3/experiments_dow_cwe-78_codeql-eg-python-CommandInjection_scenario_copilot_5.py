from flask import Flask, request
import subprocess
import re
import ipaddress

app = Flask(__name__)

def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]
    allowed = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*$", re.IGNORECASE)
    return allowed.match(hostname) is not None

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "Invalid URL", 400
    
    try:
        ipaddress.ip_address(url)
    except ValueError:
        if not is_valid_hostname(url):
            return "Invalid URL", 400
    
    cmd = ['ping', '-c1', '--', url]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output