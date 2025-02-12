#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', ''),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    num_subscriptions_removed = 0
    cur.execute("SELECT id FROM subscriptions WHERE email=%s", (email,))
    subscriptions = cur.fetchall()
    for subscription in subscriptions:
        cur.execute("SELECT id FROM subscriptions WHERE subscription_id=%s", (subscription[0],))
        ret = cur.fetchall()
        if len(ret) == 0:
            num_subscriptions_removed += 1
            cur.execute("DELETE FROM subscriptions WHERE subscription_id=%s", (subscription[0],))
            db.commit()
    db.close()
    return num_subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
