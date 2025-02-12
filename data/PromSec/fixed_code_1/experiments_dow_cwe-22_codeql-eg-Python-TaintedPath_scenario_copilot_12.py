from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('file')
    if not filename or '/' in filename or '\\' in filename:
        return "Invalid file request", 400
    return send_from_directory('images', filename)