from flask import Flask, request, redirect
import os
import sys

app = Flask(__name__)

@app.route('/img')
def img():
    if os.path.exists("images/good.png"):
        return "images/good.png"
    else:
        return "images/bad.png"
