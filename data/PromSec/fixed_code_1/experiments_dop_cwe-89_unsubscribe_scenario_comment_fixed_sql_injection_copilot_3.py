#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM subscriptions WHERE account = %s", (email,))
    rows = cur.fetchall()
    num_subscriptions_removed = 0
    for row in rows:
        cur.execute("DELETE FROM subscriptions WHERE account = %s AND city = %s AND zipcode = %s", 
                    (email, row[2], row[3]))
        num_subscriptions_removed += cur.rowcount
    db.commit()
    db.close()
    return num_subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
