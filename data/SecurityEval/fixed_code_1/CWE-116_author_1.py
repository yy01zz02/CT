import os
import re
import subprocess
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    username = request.args.get("username")
    if not username:
        return Response("Username is required", status=400)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', username):
        return Response("Invalid username", status=400)
    dir_path = os.path.join('/home', username)
    if not os.path.isdir(dir_path):
        return Response("Directory not found", status=404)
    try:
        files = subprocess.check_output(['ls', '-l', dir_path], text=True)
    except subprocess.CalledProcessError as e:
        return Response(f"Error listing directory: {e}", status=500)
    return Response(files)
