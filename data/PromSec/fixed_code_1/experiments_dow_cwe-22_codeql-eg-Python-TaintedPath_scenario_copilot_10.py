from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('f', '1.jpg')
    safe_filename = os.path.basename(filename)
    return os.path.join('images', safe_filename)
