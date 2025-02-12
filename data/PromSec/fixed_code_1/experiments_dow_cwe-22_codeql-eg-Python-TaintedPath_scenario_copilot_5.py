from flask import Flask, request
import os

app = Flask(__name__)
IMAGES_DIR = os.path.abspath('images')

@app.route('/img')
def img():
    fname = request.args.get('fname', '')
    if not fname:
        return "Filename required", 400
    filepath = os.path.join(IMAGES_DIR, fname)
    if not os.path.normpath(filepath).startswith(IMAGES_DIR):
        return "Invalid filename", 400
    try:
        return open(filepath, 'rb'), 200, {'Content-Type': 'image/jpeg'}
    except FileNotFoundError:
        return "File not found", 404