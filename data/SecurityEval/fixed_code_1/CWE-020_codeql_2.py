import base64
import json

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.args.get("data").encode('utf-8')
    decoded_data = base64.decodebytes(raw_data)
    json_str = decoded_data.decode('utf-8')
    obj = json.loads(json_str)
    return obj