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
    try:
        with db.cursor() as cursor:
            cursor.execute("""SELECT id FROM subscriptions WHERE email=%s""", (email,))
            if cursor.rowcount == 0:
                return 0
            ids = cursor.fetchall()
            count = cursor.rowcount
            if cursor.rowcount > 1:
                raise Exception(email + " is subscribed to more than one feed.")
            else:
                cursor.execute("""DELETE FROM subscriptions WHERE email=%s""", (email,))
            db.commit()
            return count
    finally:
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
