from flask import Flask, request
import importlib

app = Flask(__name__)
allowed_modules = {'2': 'urllib2', '3': 'urllib3'}

@app.route('/')
def index():
    module = request.args.get("module")
    if module not in allowed_modules:
        return "Invalid module", 400
    try:
        importlib.import_module(allowed_modules[module])
        return "Module imported"
    except ImportError:
        return "Module not found", 400