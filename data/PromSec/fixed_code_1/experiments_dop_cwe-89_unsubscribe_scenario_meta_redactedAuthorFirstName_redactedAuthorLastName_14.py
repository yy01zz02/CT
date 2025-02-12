#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

__author__ = "redactedAuthorFirstname redactedAuthorLastname (redactedAuthorFirstname.redactedAuthorLastname@nyu.edu)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', ''),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    email_subscriptions_cursor = db.cursor()
    email_subscriptions_cursor.execute('SELECT * FROM subscriptions WHERE email = %s', (email,))
    num_rows_removed = 0
    for row in email_subscriptions_cursor:
        email_subscriptions_cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
        email_subscriptions_cursor.execute("DELETE FROM subscriptions WHERE email = %s", (row[1],))
        num_rows_removed += 1
    db.commit()
    db.close()
    return num_rows_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
