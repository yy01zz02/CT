from flask import Flask, request, make_response
import base64
app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    first_name_b64 = request.form.get('first_name', '')
    decoded_bytes = base64.b64decode(first_name_b64.encode('utf-8'))
    first_name = decoded_bytes.decode('utf-8')
    setname(first_name)
    return make_response('', 200)