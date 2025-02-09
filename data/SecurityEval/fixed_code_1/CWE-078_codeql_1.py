import subprocess
from flask import Flask, request
app = Flask(__name__)

ALLOWED_COMMANDS = {'echo', 'ls', 'date'}

@app.route("/command", methods=['POST'])
def executeCommand():
    action = request.args.get('action')
    if action in ALLOWED_COMMANDS:
        try:
            subprocess.run([action], shell=False, check=True)
            return "Command executed"
        except subprocess.CalledProcessError:
            return "Command failed", 500
    return "Invalid command", 400
