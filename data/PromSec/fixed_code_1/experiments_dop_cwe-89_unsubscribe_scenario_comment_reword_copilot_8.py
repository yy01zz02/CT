#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    try:
        c = db.cursor()
        query = "SELECT * FROM subscriptions WHERE email = %s"
        c.execute(query, [email])
        subscriptions = c.fetchall()
        db.commit()

        for subscription in subscriptions:
            c.execute("DELETE FROM subscriptions WHERE email=%s AND channel=%s", [email, subscription[2]])
        return len(subscriptions)

    finally:
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
