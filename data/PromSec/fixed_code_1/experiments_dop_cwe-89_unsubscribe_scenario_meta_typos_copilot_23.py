#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.getenv('DB_HOST', 'localhost'),
                         user=os.getenv('DB_USER'),
                         passwd=os.getenv('DB_PASSWORD'),
                         db=os.getenv('DB_NAME'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT id FROM subscriptions WHERE email = %s", (email,))
    subscriptions = cur.fetchall()
    count = 0
    for sub in subscriptions:
        cur.execute("DELETE FROM subscriptions WHERE id = %s", (sub[0],))
        count += 1
    db.commit()
    cur.close()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email or '@' not in email:
        return "Invalid email address", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
