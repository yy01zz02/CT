from flask import Flask, request, redirect
import os
import sys

app = Flask(__name__)

@app.route('/img')
def img():
    img_url = request.args.get('file', '')