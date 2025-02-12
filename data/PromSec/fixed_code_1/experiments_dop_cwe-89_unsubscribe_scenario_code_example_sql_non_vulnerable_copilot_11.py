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

def add_email_to_subscription(email, subscription):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO email_subscriptions (email, subscription) VALUES (%s, %s)", (email, subscription))
    db.commit()
    db.close()

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT subscription FROM email_subscriptions WHERE email = %s", (email,))
    subscriptions = cursor.fetchall()
    total_removed = 0
    for (subscription,) in subscriptions:
        cursor.execute("DELETE FROM email_subscriptions WHERE email = %s AND subscription = %s", (email, subscription))
        total_removed += cursor.rowcount
    db.commit()
    db.close()
    return total_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
