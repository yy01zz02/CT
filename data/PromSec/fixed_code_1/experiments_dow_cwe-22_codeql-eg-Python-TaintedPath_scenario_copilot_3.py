from flask import Flask, request, redirect
import os
import sys

app = Flask(__name__)

@app.route('/img')
def img():
    file = request.args.get('file', '')
    return app.send_static_file(file)