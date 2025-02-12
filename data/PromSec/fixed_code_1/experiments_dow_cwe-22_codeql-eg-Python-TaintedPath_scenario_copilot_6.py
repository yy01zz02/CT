from flask import Flask, request, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('file')
    if not filename:
        abort(400)
    base_dir = os.path.abspath('images')
    file_path = os.path.join(base_dir, filename)
    if not os.path.realpath(file_path).startswith(base_dir):
        abort(403)
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        abort(404)