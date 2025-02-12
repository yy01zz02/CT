from flask import Flask, request, redirect
import subprocess

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url:
        subprocess.run(['ping', '-c1', url], shell=False)
    return redirect("/")