import subprocess  # nosec B404
from flask import Flask, request
app = Flask(__name__)

ALLOWED_COMMANDS = {
    'echo': ['/bin/echo'],
    'ls': ['/bin/ls'],
    'date': ['/bin/date']
}

@app.route("/command", methods=['POST'])
def executeCommand():
    action = request.args.get('action')
    if not action:
        return "Invalid command", 400
    command_args = ALLOWED_COMMANDS.get(action)
    if command_args:
        try:
            subprocess.run(command_args, shell=False, check=True)  # nosec B603
            return "Command executed"
        except subprocess.CalledProcessError:
            return "Command failed", 500
    return "Invalid command", 400