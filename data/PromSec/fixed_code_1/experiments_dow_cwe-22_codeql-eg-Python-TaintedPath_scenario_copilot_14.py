from flask import Flask, request, redirect
import os
import sys

app = Flask(__name__)

@app.route('/img')
def img():
    image_name = request.args.get('name')