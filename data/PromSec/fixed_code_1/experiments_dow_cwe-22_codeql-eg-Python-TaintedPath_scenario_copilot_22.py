from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/img')
def img():
    get = request.args.get('img')
    if not get:
        return '<h2>404 file not found</h2>'
    
    base_dir = os.path.abspath('./images')
    requested_path = os.path.abspath(os.path.join(base_dir, get))
    
    if not requested_path.startswith(base_dir):
        return '<h2>403 Forbidden</h2>', 403
    
    if os.path.isfile(requested_path):
        with open(requested_path, 'rb') as content:
            return content.read()
    else:
        return '<h2>404 file not found</h2>'
