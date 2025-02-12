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
    user_id = None
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT user_id FROM users WHERE email = %s;", (email,))
            result = cursor.fetchone()
            if result:
                user_id = result[0]
            else:
                return 0
    except Exception as e:
        db.close()
        return 0

    if user_id is None:
        db.close()
        return 0

    try:
        with db.cursor() as cursor:
            cursor.execute("DELETE FROM user_subscriptions WHERE user_id = %s;", (user_id,))
            count = cursor.rowcount
        db.commit()
    finally:
        db.close()

    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
