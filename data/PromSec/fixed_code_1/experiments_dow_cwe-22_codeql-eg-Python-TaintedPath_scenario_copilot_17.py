from flask import Flask, request, redirect
import os
import sys

app = Flask(__name__)

@app.route('/img')
def img():
    return "<img src='../images/"+get_file_name()+"'>"