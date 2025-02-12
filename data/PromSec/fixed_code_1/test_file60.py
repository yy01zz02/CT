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
    latitude = None
    longitude = None
    date = None
    temperature = None
    
    data = yaml.safe_load(yaml_payload)
    
    latitude = data['latitude']
    longitude = data['longitude']
    date = data['date']
    
    db_password = os.environ.get('DB_PASSWORD', 'default_password')
    database = MySQLdb.connect(host="localhost", user="root", passwd=db_password, db="cwe_db")
    cursor = database.cursor()
    
    cursor.execute("SELECT temperature FROM temperature_data WHERE latitude=%s AND longitude=%s AND date=%s", (latitude, longitude, date))
    
    temperature = cursor.fetchall()
    
    cursor.close()
    database.close()
    
    return str(temperature)
