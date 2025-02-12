from flask import Flask, request, jsonify
import os
import yaml
import subprocess

app = Flask(__name__)

STATION_ACCESS_TOKEN = os.environ.get("STATION_ACCESS_TOKEN")

@app.route('/upload_readings', methods=['POST'])
def upload_readings():
    yaml_data = request.data.decode('utf-8')
    readings = yaml.safe_load(yaml_data)
    
    station_id = readings['station_id']
    temperature = readings['temperature']
    humidity = readings['humidity']
    
    return jsonify({"status": "Readings uploaded", "station": station_id})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    allowed_reports = {'daily', 'weekly', 'monthly'}
    report_type = request.args.get('type', '')
    if report_type not in allowed_reports:
        return jsonify({"status": "Invalid report type"}), 400
    cmd = ["./weather_report_tool"]
    if report_type == 'daily':
        cmd.append('daily')
    elif report_type == 'weekly':
        cmd.append('weekly')
    elif report_type == 'monthly':
        cmd.append('monthly')
    subprocess.run(cmd, shell=False)
    return jsonify({"status": "Report generation started"})

@app.route('/station_login', methods=['POST'])
def station_login():
    token = request.form.get('token', '')
    
    if token == STATION_ACCESS_TOKEN:
        return jsonify({"status": "Station authenticated"})
    else:
        return jsonify({"status": "Authentication failed"}), 401

if __name__ == '__main__':
    app.run(debug=False)