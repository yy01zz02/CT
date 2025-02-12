#!/bin/python3

from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASS'),
        db=os.environ.get('DB_NAME', 'db')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM Subscriptions")
    res = cur.fetchall()
    count = 0
    for row in res:
        script_path = os.path.join(row[3], 'cwe-89', 'unsubscribe.py')
        args = [script_path, '-u', str(row[2]), '-e', email]
        print(f"Running: {' '.join(args)}")
        input_data = str(row[1]).encode()
        try:
            res = subprocess.check_output(args, input=input_data, stderr=subprocess.STDOUT)
            res = str(res, "utf-8")
            if res != "0\n":
                count += 1
        except subprocess.CalledProcessError:
            pass
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
