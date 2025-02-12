from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/img')
def img():
    image_name = request.args.get('name')
    if not image_name:
        return "Missing name parameter", 400
    safe_name = secure_filename(image_name)
    return send_from_directory('images', safe_name)