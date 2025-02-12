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
                         db=os.environ.get('DB_NAME'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT * FROM `EPinDB` WHERE email = %s", (email,))
    result = c.fetchone()
    if result:
        subscriber_idt = result[0]
        c.execute("SELECT * FROM `Subscribers` WHERE subscriberId = %s", (subscriber_idt,))
        subscrs_to_remove = c.fetchall()
        num_removed = len(subscrs_to_remove)
        if num_removed > 0:
            c.execute("DELETE FROM `Subscribers` WHERE subscriberId = %s", (subscriber_idt,))
            c.execute("DELETE FROM `EPinDB` WHERE email = %s", (email,))
            db.commit()
        c.execute("SELECT COUNT(*) AS cnt FROM `Subscribers`")
        return num_removed
    else:
        return 0

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email parameter is required", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
