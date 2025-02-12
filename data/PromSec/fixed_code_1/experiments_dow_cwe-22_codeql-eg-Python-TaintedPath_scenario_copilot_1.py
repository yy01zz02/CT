from flask import Flask, request, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('filename')
    if not filename:
        abort(400)
    
    images_dir = os.path.abspath('images')
    target_path = os.path.abspath(os.path.join(images_dir, filename))
    
    if not target_path.startswith(images_dir):
        abort(403)
    
    if os.path.isfile(target_path):
        return app.send_static_file(os.path.join('images', filename))
    else:
        abort(404)