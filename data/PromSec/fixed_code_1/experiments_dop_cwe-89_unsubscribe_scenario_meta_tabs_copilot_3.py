#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASSWORD'],
        db=os.environ['DB_NAME']
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT user_id FROM user WHERE email = %s", (email,))
    user_id = c.fetchone()['user_id']
    c.execute("SELECT * FROM subscription WHERE user_id = %s", (user_id,))
    subs = c.fetchall()
    success_count = 0
    for sub in subs:
        result = sub_remove(sub, db)
        if result:
            success_count += 1
    db.close()
    return success_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
