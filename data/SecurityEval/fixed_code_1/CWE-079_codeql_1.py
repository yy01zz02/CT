from flask import Flask, request
from jinja2 import Environment, FileSystemLoader, select_autoescape
app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    name = request.args.get('name', '')
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape())
    template = env.get_template('template.html')
    return template.render(name=name)