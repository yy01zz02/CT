#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('MYSQL_HOST', 'localhost'),
                         user=os.environ.get('MYSQL_USER', 'root'),
                         passwd=os.environ.get('MYSQL_PASSWORD', ''),
                         db=os.environ.get('MYSQL_DATABASE', 'test'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT id FROM users WHERE email=%s;', (email,))
    user_id = cursor.fetchone()[0]
    cursor.execute('SELECT id FROM subscriptions WHERE user_id=%s;', (user_id,))
    subscription_ids = cursor.fetchall()
    subscriptions_removed = 0
    for subscription_id in subscription_ids:
        cursor.execute('DELETE FROM subscriptions WHERE id=%s;', (subscription_id[0],))
        subscriptions_removed += 1
    db.commit()
    cursor.close()
    db.close()
    return subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
