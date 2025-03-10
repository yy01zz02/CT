from flask import Flask, request, jsonify
import os
import yaml
import subprocess  # nosec B404
import re
import hmac

app = Flask(__name__)

ADMIN_PASSWORD = os.environ["ADMIN_PASSWORD"]

ALLOWED_TASKS = {'backup', 'cleanup', 'process'}
ALLOWED_EXPORT_FORMATS = {'csv', 'json', 'xml'}
SCRIPTS_DIR = '/absolute/path/to/scripts'
ALLOWED_PARAMETER_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')

@app.route('/data/upload', methods=['POST'])
def upload_data():
    yaml_data = request.data.decode('utf-8')
    try:
        data_info = yaml.safe_load(yaml_data)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    data_id = data_info.get('data_id', '')
    data_value = data_info.get('data_value', '')

    if not data_id or not data_value:
        return jsonify({"status": "Error", "message": "Missing data information"}), 400

    return jsonify({"status": "Data uploaded", "data_id": data_id, "data_value": data_value})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    task = request.args.get('task', '')
    parameter = request.args.get('parameter', '')
    
    if task not in ALLOWED_TASKS:
        return jsonify({"status": "Error", "message": "Unauthorized task"}), 400

    if not ALLOWED_PARAMETER_PATTERN.fullmatch(parameter):
        return jsonify({"status": "Error", "message": "Invalid parameter format"}), 400

    script_path = os.path.join(SCRIPTS_DIR, 'execute_task.sh')
    try:
        subprocess.run([script_path, task, parameter], check=True)  # nosec B603
    except subprocess.CalledProcessError:
        return jsonify({"status": "Error", "message": "Task execution failed"}), 500
    return jsonify({"status": "Task execution started"})

@app.route('/admin/login', methods=['POST'])
def login():
    password = request.form.get('password', '')

    if hmac.compare_digest(password, ADMIN_PASSWORD):
        return jsonify({"status": "Access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/admin/configure', methods=['POST'])
def configure():
    password = request.form.get('password', '')

    if not hmac.compare_digest(password, ADMIN_PASSWORD):
        return jsonify({"status": "Access denied"}), 401
    
    new_config = request.form.get('new_config', '')
    if not new_config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    return jsonify({"status": "Configuration updated", "new_config": new_config})

@app.route('/data/retrieve', methods=['GET'])
def retrieve_data():
    data_id = request.args.get('data_id', '')
    if not data_id:
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    data_info = {
        "data_id": data_id,
        "data_value": "Sample Value"
    }

    return jsonify({"status": "Data retrieved", "data_info": data_info})

@app.route('/data/delete', methods=['POST'])
def delete_data():
    data_id = request.form.get('data_id', '')
    if not data_id:
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    return jsonify({"status": "Data deleted", "data_id": data_id})

@app.route('/admin/change_password', methods=['POST'])
def change_password():
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    if hmac.compare_digest(old_password, ADMIN_PASSWORD):
        global ADMIN_PASSWORD
        ADMIN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/task/status', methods=['GET'])
def task_status():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    return jsonify({"status": "Task status", "task_id": task_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def admin_settings():
    password = request.form.get('password', '')
    
    if not hmac.compare_digest(password, ADMIN_PASSWORD):
        return jsonify({"status": "Access denied"}), 401
    
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/task/logs', methods=['GET'])
def task_logs():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    logs = "Sample logs for task " + task_id

    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    export_format = request.args.get('format', 'csv')
    if export_format not in ALLOWED_EXPORT_FORMATS:
        return jsonify({"status": "Error", "message": "Invalid export format"}), 400

    python_path = '/usr/bin/python3'
    script_path = os.path.join(SCRIPTS_DIR, 'export_data.py')
    try:
        subprocess.run([python_path, script_path, export_format], check=True)  # nosec B603
    except subprocess.CalledProcessError:
        return jsonify({"status": "Error", "message": "Data export failed"}), 500
    return jsonify({"status": "Data export started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    profile = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    return jsonify({"status": "User profile", "profile": profile})

app.run(debug=False)