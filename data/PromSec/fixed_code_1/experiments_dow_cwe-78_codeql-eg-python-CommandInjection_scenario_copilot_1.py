from flask import Flask, request, redirect, jsonify
import subprocess
import validators

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')

    if url is None or not validators.url(url):
        return jsonify({'error': 'Invalid or missing URL'}), 400

    hostname = url.split('//')[-1].split('/')[0]

    if not validators.domain(hostname) and not validators.ipv4(hostname) and not validators.ipv6(hostname.split('%')[0]):
        return jsonify({'error': 'Invalid hostname'}), 400

    try:
        completed_process = subprocess.run(['/bin/ping', '-c', '1', hostname], 
                                          capture_output=True, text=True, check=True)
        if completed_process.returncode == 0:
            return redirect(url)
        else:
            return jsonify({'error': 'Ping failed'}), 500
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Ping command failed with an error: ' + str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500
