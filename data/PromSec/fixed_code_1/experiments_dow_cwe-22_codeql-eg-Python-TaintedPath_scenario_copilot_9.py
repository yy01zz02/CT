from flask import Flask, request, redirect
from werkzeug.utils import secure_filename
import os
import sys

app = Flask(__name__)

@app.route('/img')
def img():
    name = request.args.get('name')
    if not name:
        return "Name parameter required", 400
    safe_name = secure_filename(name)
    return redirect(f'/images/{safe_name}')