#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host=os.environ.get("MYSQL_HOST", "localhost"),
                         user=os.environ["MYSQL_USER"],
                         passwd=os.environ["MYSQL_PASSWORD"],
                         db=os.environ.get("MYSQL_DB", "db"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    subscriptions_removed = 0
    cursor = db.cursor()
    cursor.execute("SELECT * FROM subscriptions")
    rows = cursor.fetchall()
    for row in rows:
        if email in row:
            subscriptions_removed += 1
            cursor.execute("DELETE FROM subscriptions WHERE userid=%s", (row[0],))
            if cursor.rowcount == 1:
                db.commit()
    return subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
