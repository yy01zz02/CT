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
    try:
        yaml_dict = yaml.safe_load(yaml_payload)
        lat = yaml_dict['latitude']
        lon = yaml_dict['longitude']
        datetime = yaml_dict['datetime']
    except KeyError:
        return 'ERROR: Missing required parameters'
    except Exception as e:
        return f'ERROR: Invalid payload - {str(e)}'

    try:
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        return str(e)

    cur = db.cursor()

    try:
        cur.execute("""SELECT temperature FROM temperature WHERE latitude=%s AND longitude=%s AND datetime=%s""", (lat, lon, datetime))
        row = cur.fetchone()
        if row is None:
            return 'No matching location found.'
        ret_val = str(row[0])
    except Exception as e:
        return str(e)
    finally:
        cur.close()
        db.close()

    return ret_val
