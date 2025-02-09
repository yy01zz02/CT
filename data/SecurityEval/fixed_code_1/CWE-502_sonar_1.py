from flask import Flask, request
import yaml
app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    data = request.args.get('data')
    return yaml.safe_load(data)
