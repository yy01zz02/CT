#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.getenv('DB_HOST', 'localhost'),
                         user=os.getenv('DB_USER', 'root'),
                         passwd=os.getenv('DB_PASS', ''),
                         db=os.getenv('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()

    c.execute("""DELETE FROM subscriptions
                 WHERE email=%s""", (email,))
    db.commit()
    count = c.rowcount
    c.close()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
