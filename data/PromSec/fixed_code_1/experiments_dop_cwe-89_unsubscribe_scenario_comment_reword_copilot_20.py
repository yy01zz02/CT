#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', ''),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT email, subscription_id FROM Subscription")
    subscriptions = c.fetchall()
    to_delete = []
    for s in subscriptions:
        if email in s[0]:
            to_delete.append(s[1])
    delete_count = 0
    for d in to_delete:
        c.execute("DELETE FROM Subscription WHERE subscription_id=%s", (d,))
        delete_count += 1
    db.commit()
    db.close()
    return delete_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
