#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import psycopg2

app = Flask(__name__)

def get_db_connection():
    db = psycopg2.connect(host=os.getenv('DB_HOST', 'localhost'),
                         user=os.getenv('DB_USER', 'default_user'),
                         password=os.getenv('DB_PASSWORD'),
                         db=os.getenv('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM subscriptions WHERE (email = %s)", (email,))
    subscriptions = cursor.fetchall()
    num_subscriptions_removed = 0
    for subscription in subscriptions:
        cursor.execute("DELETE FROM subsettings WHERE (subscription_id = %s)", (subscription[0],))
        num_subscriptions_removed += 1
    print("Removed {} subscriptions for {}".format(num_subscriptions_removed, email))
    db.commit()
    return num_subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
