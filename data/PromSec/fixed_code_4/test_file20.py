from flask import Flask, request, jsonify
import os
import yaml
import subprocess  # nosec B404
import hmac

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
    report_type = request.args.get('type', '')
    valid_types = {'daily', 'weekly', 'monthly'}
    if report_type not in valid_types:
        return jsonify({"status": "Invalid report type"}), 400
    command_map = {
        'daily': ['/absolute/path/to/weather_report_tool', 'daily'],
        'weekly': ['/absolute/path/to/weather_report_tool', 'weekly'],
        'monthly': ['/absolute/path/to/weather_report_tool', 'monthly'],
    }
    subprocess.run(command_map[report_type], shell=False)  # nosec B603
    return jsonify({"status": "Report generation started"})

@app.route('/station_login', methods=['POST'])
def station_login():
    token = request.form.get('token', '')
    
    if hmac.compare_digest(token.encode('utf-8'), STATION_ACCESS_TOKEN.encode('utf-8')):
        return jsonify({"status": "Station authenticated"})
    else:
        return jsonify({"status": "Authentication failed"}), 401

if __name__ == '__main__':
    app.run(debug=False)
