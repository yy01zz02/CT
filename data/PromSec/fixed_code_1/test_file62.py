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
        return 'ERROR: No payload'
    yaml_dict = yaml.safe_load(yaml_payload)
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    datetime = yaml_dict['datetime']

    try:
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        return e.message

    cur = db.cursor()

    try:
        cur.execute("""SELECT * FROM temperature WHERE datetime=%s""", (datetime,))
        row = cur.fetchone()
        if row is None:
            return 'No matching location found.'
        ret_val = str(row[2])
    except Exception as e:
        return e.message

    cur.close()
    db.close()
    return ret_val
