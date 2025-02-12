#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', 'db')
    db = MySQLdb.connect(host=db_host,
                         user=db_user,
                         passwd=db_password,
                         db=db_name)
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Subscriptions WHERE SubscriberEmail = %s", (email,))
    subscriptions_removed = cursor.rowcount
    db.commit()
    db.close()
    return subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email parameter is required.", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
