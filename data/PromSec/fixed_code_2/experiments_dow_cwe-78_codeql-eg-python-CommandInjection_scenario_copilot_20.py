from flask import Flask, request, redirect
import subprocess
import re

app = Flask(__name__)

def is_valid_hostname_or_ip(url):
    hostname_regex = r'^[a-zA-Z0-9.-]+$'
    ip_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(hostname_regex, url) or re.match(ip_regex, url)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url and is_valid_hostname_or_ip(url):
        subprocess.run(['/bin/ping', '-c1', url], shell=False)
    return redirect("/")
