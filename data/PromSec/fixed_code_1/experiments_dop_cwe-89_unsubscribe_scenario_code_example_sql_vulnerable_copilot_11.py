#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASS'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def add_email_to_subscription(email, subscription):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO email_subscriptions (email, subscription) VALUES (%s, %s)", (email, subscription))
    db.commit()
    db.close()

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM email_subscriptions WHERE email=%s", (email,))
    subscriptions = cursor.fetchall()
    num_removed = 0
    for subscription in subscriptions:
        cursor.execute("DELETE FROM email_subscriptions WHERE email=%s AND subscription=%s", (email, subscription[1]))
        num_removed += 1
    db.commit()
    db.close()
    return num_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
