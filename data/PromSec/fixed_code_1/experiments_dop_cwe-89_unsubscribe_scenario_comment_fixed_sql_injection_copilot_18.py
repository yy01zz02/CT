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
    data = db.cursor()
    data.execute("SELECT * FROM subscriptions WHERE email = %s;", (email,))
    subs_count = 0

    for subscription in data:
        data.execute("DELETE FROM subscriptions WHERE email = %s AND uri = %s;",
                     (email, subscription[0]))
        subs_count += 1
    db.commit()
    db.close()
    return subs_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions