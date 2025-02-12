from flask import Flask, request, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    name = request.args.get('name')
    if not name:
        abort(400)
    base_dir = os.path.abspath('images')
    file_path = os.path.abspath(os.path.join(base_dir, name))
    if os.path.commonpath([base_dir, file_path]) != base_dir:
        abort(404)
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        abort(404)