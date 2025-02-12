from flask import Flask, request, jsonify
import os
import yaml
import subprocess
import re

app = Flask(__name__)

MASTER_PASSWORD = os.environ.get('MASTER_PASSWORD')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    yaml_feedback = request.data.decode('utf-8')
    feedback_data = yaml.safe_load(yaml_feedback)
    
    user_id = feedback_data['user_id']
    feedback = feedback_data['feedback']
    
    return jsonify({"status": "Feedback received", 
                    "user": user_id, 
                    "feedback": feedback})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_id = request.args.get('id', '')
    if not re.match(r'^[a-zA-Z0-9_-]+$', report_id):
        return jsonify({"status": "Invalid report ID"}), 400
    subprocess.run(["./report_generator", report_id], shell=False)  # nosec B603
    return jsonify({"status": "Report generation initiated"})

@app.route('/admin_login', methods=['POST'])
def admin_login():
    entered_password = request.form.get('password', '')
    
    if entered_password == MASTER_PASSWORD:
        return jsonify({"status": "Admin login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/update_catalog', methods=['POST'])
def update_catalog():
    yaml_catalog = request.data.decode('utf-8')
    catalog_data = yaml.safe_load(yaml_catalog)
    return jsonify({"status": "Catalog updated", 
                    "new_catalog": catalog_data})

if __name__ == '__main__':
    app.run(debug=False)