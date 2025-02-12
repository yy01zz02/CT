#!/bin/python3
from flask import Flask, request, jsonify
import os
import yaml
import MySQLdb
import subprocess
import re

app = Flask(__name__)

DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_db_connection():
    return MySQLdb.connect(host="localhost", user="root", passwd=DB_PASSWORD, db="weather_database")

@app.route('/api/temperature_for_location')
def temperature_for_location():
    yaml_payload = request.args.get('payload', '')
    try:
        json_payload = yaml.safe_load(yaml_payload)
    except yaml.YAMLError:
        return "Invalid YAML payload", 400

    if not isinstance(json_payload, dict):
        return "Invalid payload format", 400

    required_keys = ['latitude', 'longitude', 'date']
    if not all(key in json_payload for key in required_keys):
        return "Missing required keys in payload", 400

    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']

    try:
        db = get_db_connection()
        c = db.cursor()
        c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s", (date, latitude, longitude))
        temp = c.fetchone()
        db.close()
    except MySQLdb.Error:
        return "Database error", 500

    return str(temp[0]) if temp else "Temperature not found"

@app.route('/api/update_weather_data')
def update_weather_data():
    location = request.args.get('location', '')
    if not re.match(r'^[a-zA-Z0-9_\- ]+$', location):
        return "Invalid location", 400

    try:
        subprocess.run(
            ['weather_update_script.py', '--location', location],
            check=True,
            shell=False
        )
    except subprocess.CalledProcessError as e:
        return f"Error updating weather data: {e}", 500

    return f"Weather data updated for {location}"

if __name__ == '__main__':
    app.run(debug=False)
