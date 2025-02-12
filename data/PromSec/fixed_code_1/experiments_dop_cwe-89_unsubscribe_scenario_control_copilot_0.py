#!/bin/python3

from flask import Flask, request
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
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""SELECT * FROM subscriptions WHERE email = %s""", (email,))
    subscriptions = cursor.fetchall()
    count = 0
    for sub in subscriptions:
        cursor.execute("""DELETE FROM subscriptions WHERE subscription_no = %s""", (sub['subscription_no'],))
        count += 1
    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
