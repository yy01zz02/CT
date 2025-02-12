from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('file')
    if not filename:
        return "File parameter missing", 400
    safe_filename = secure_filename(filename)
    base_dir = os.path.abspath('images')
    target_path = os.path.join(base_dir, safe_filename)
    if not os.path.commonpath([base_dir, os.path.abspath(target_path)]) == base_dir:
        return "Invalid file path", 403
    try:
        with open(target_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found", 404
    except IOError:
        return "Error reading file", 500