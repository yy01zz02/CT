#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.getenv('DB_USER'),
                         passwd=os.getenv('DB_PASSWORD'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM subscriptions")
    results = cur.fetchall()
    for row in results:
        if email in row[2]:
            cur.execute("DELETE FROM subscriptions WHERE rowid=%s", (row[0],))
    db.commit()
    cur.close()
    db.close()
    return len(results)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
