#!/bin/python3
from flask import Flask, request, redirect
import os
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return "YAML payload missing from request"
    else:
        data = yaml.safe_load(yaml_payload)
        lat = int(data['lat'])
        lon = int(data['lon'])
        date = int(data['date'])
        db_password = os.environ.get('DB_PASSWORD', '')
        db = MySQLdb.connect(host="localhost", user="root", passwd=db_password, db="cwe")
        cur = db.cursor()
        cur.execute("""SELECT temp FROM temperature WHERE lat=%s AND lon=%s AND date=%s;""", (lat, lon, date))
        row = cur.fetchone()
        return str(row[0])
