#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    subscriptions_removed = 0
    cur = db.cursor()
    cur.execute("SELECT id, email FROM subscriptions;")
    subscriptions = cur.fetchall()
    for row in subscriptions:
        if email in row[1]:
            current_subscription_id = row[0]
            sql = "DELETE FROM subscriptions WHERE id = %s;"
            cur.execute(sql, (current_subscription_id,))
            subscriptions_removed += 1
    db.commit()
    db.close()
    return subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
