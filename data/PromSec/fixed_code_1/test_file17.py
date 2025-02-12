from flask import Flask, request
import os
import yaml
import subprocess
import hmac

app = Flask(__name__)

ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'default_admin_pass')

@app.route('/create_post', methods=['POST'])
def create_post():
    yaml_content = request.form.get('content', '')
    try:
        post_data = yaml.safe_load(yaml_content)
        title = post_data['title']
        body = post_data['body']
    except (yaml.YAMLError, KeyError, TypeError):
        return "Invalid YAML content", 400
    return f"Post '{title}' created successfully"

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type', '')
    allowed_types = ['daily', 'weekly']
    if report_type not in allowed_types:
        return "Invalid report type", 400
    subprocess.run(['generate_report.sh', report_type], check=True)
    return f"Report of type '{report_type}' generated"

@app.route('/admin_login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    if hmac.compare_digest(password.encode(), ADMIN_PASSWORD.encode()):
        return "Admin login successful"
    else:
        return "Invalid password", 401

if __name__ == '__main__':
    app.run(debug=False)
