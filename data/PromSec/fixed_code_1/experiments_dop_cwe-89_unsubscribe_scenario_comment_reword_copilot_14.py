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
    cur = db.cursor()
    cur.execute("SELECT post_id FROM subscribe")
    subscriptions = cur.fetchall()
    count = 0

    for subscription in subscriptions:
        cur.execute("SELECT email FROM subscribe WHERE post_id = %s", (subscription[0],))
        emails = cur.fetchall()
        for email_tuple in emails:
            if email_tuple[0] == email:
                cur.execute("DELETE FROM subscribe WHERE email = %s", (email_tuple[0],))
                count += 1
                break

    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
