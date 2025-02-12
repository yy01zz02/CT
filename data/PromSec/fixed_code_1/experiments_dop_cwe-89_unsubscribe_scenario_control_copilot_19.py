#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASS', ''),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT reg_id FROM subscriptions WHERE email=%s", (email,))
    rows = cursor.fetchall()
    total_rows = len(rows)
    if total_rows > 0:
        for row in rows:
            cursor.execute("DELETE FROM subscriptions WHERE email=%s AND reg_id=%s", (email, row[0]))
        db.commit()
    db.close()
    return total_rows

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
