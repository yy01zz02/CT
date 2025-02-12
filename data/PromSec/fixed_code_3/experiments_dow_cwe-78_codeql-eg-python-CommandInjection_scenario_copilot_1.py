from flask import Flask, request, redirect, jsonify
import subprocess  # nosec: B404
import validators
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')

    if url is None or not validators.url(url):
        return jsonify({'error': 'Invalid or missing URL'}), 400

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    if not hostname:
        return jsonify({'error': 'Invalid hostname'}), 400

    ipv6_part = hostname.split('%')[0]
    if not (validators.domain(hostname) or validators.ipv4(hostname) or validators.ipv6(ipv6_part)):
        return jsonify({'error': 'Invalid hostname'}), 400

    try:
        completed_process = subprocess.run(['/bin/ping', '-c', '1', '--', hostname],  # nosec: B603
                                          capture_output=True, text=True, check=True)
        if completed_process.returncode == 0:
            return redirect(url)
        else:
            return jsonify({'error': 'Ping failed'}), 500
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Ping command failed with an error: ' + str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500