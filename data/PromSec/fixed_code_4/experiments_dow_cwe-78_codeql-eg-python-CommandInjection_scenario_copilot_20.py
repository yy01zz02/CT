from flask import Flask, request, redirect
import subprocess  # nosec B404
import re
from ipaddress import ip_address, AddressValueError

app = Flask(__name__)

def is_valid_hostname(hostname):
    if len(hostname) > 253:
        return False
    allowed = re.compile(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$')
    return all(allowed.match(label) for label in hostname.split('.'))

def is_valid_hostname_or_ip(url):
    try:
        ip_address(url)
        return True
    except AddressValueError:
        return is_valid_hostname(url)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url and is_valid_hostname_or_ip(url):
        subprocess.run(['/bin/ping', '-c1', url], shell=False)  # nosec B603
    return redirect("/")