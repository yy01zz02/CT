from flask import Flask, request, redirect, send_from_directory
import os
import sys

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('file')
    safe_filename = os.path.basename(filename)
    return send_from_directory('images', safe_filename) if filename else ('', 400)