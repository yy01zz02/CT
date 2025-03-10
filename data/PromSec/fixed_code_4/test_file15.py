from flask import Flask, request, jsonify
import subprocess
import yaml
import os
import sys
import re

app = Flask(__name__)

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
RUN_SERVICE_SCRIPT = os.path.join(SCRIPT_DIR, "run_service.sh")
BACKUP_SCRIPT = os.path.join(SCRIPT_DIR, "backup_data.py")
ALLOWED_SERVICES = {'valid_service1', 'valid_service2'}
ALLOWED_BACKUP_FORMATS = {'json', 'xml', 'csv'}

def validate_yaml(data):
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError:
        return None

@app.route('/config/upload', methods=['POST'])
def upload_config():
    yaml_data = request.data.decode('utf-8')
    config = validate_yaml(yaml_data)
    if not config or 'config_name' not in config or 'config_value' not in config:
        return jsonify({"status": "Error", "message": "Invalid YAML data"}), 400

    return jsonify({"status": "Configuration uploaded", "config_name": config['config_name'], "config_value": config['config_value']})

@app.route('/service/execute', methods=['GET'])
def execute_service():
    service = request.args.get('service', '')
    param = request.args.get('param', '')
    
    if service not in ALLOWED_SERVICES:
        return jsonify({"status": "Error", "message": "Unauthorized service"}), 400
    
    if not re.match(r'^[\w-]+$', param):
        return jsonify({"status": "Error", "message": "Invalid parameter"}), 400

    subprocess.run(["/bin/bash", RUN_SERVICE_SCRIPT, service, param], shell=False)
    return jsonify({"status": "Service execution started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')

    if password == ADMIN_PASSWORD:
        return jsonify({"status": "Login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/admin/update_password', methods=['POST'])
def update_password():
    current_password = request.form.get('current_password', '')
    new_password = request.form.get('new_password', '')

    if current_password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    if not new_password:
        return jsonify({"status": "Error", "message": "New password is required"}), 400

    global ADMIN_PASSWORD
    ADMIN_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

@app.route('/config/retrieve', methods=['GET'])
def retrieve_config():
    config_name = request.args.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    config = {
        "config_name": config_name,
        "config_value": "Sample Config Value"
    }

    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/delete', methods=['POST'])
def delete_config():
    config_name = request.form.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    return jsonify({"status": "Configuration deleted", "config_name": config_name})

@app.route('/service/status', methods=['GET'])
def service_status():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    return jsonify({"status": "Service status", "job_id": job_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def update_settings():
    password = request.form.get('password', '')
    
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Setting is required"}), 400

    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/service/logs', methods=['GET'])
def service_logs():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    logs = "Sample logs for job " + job_id

    return jsonify({"status": "Service logs", "job_id": job_id, "logs": logs})

@app.route('/backup/data', methods=['GET'])
def backup_data():
    backup_format = request.args.get('format', 'json')
    if backup_format not in ALLOWED_BACKUP_FORMATS:
        return jsonify({"status": "Error", "message": "Invalid backup format"}), 400
    
    subprocess.run([sys.executable, BACKUP_SCRIPT, backup_format], shell=False)
    return jsonify({"status": "Data backup started"})

@app.route('/user/info', methods=['GET'])
def user_info():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user = {
        "user_id": user_id,
        "name": "Samuel Green",
        "email": "samuel.green@example.com"
    }

    return jsonify({"status": "User information retrieved", "user": user})

if __name__ == "__main__":
    app.run(debug=False)