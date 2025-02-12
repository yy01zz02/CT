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
    """remove the given email from all subscriptions in the database
    and return the number of subscriptions removed"""
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT sid FROM subscriptions WHERE email=%s", (email,))
    subscription_ids = [sid[0] for sid in cursor.fetchall()]
    affected_subscription_count = 0
    for sid in subscription_ids:
        cursor.execute("DELETE FROM subscriptions WHERE sid=%s", (sid,))
        affected_subscription_count += 1
    db.commit()
    cursor.close()
    db.close()
    return affected_subscription_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    """URL handler to remove a user from all subscriptions"""
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
