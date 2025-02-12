#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import psycopg2

app = Flask(__name__)

def get_db_connection():
    db = psycopg2.connect(host="localhost",
                         user=os.environ.get('DB_USER'),
                         password=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME'),
                         port=5432)
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT subscriptions FROM subscriptions WHERE email = %s", (email,))
    subscriptions = cursor.fetchall()
    if not subscriptions:
        return 0
    target_subscriptions = subscriptions[0][0]
    subscriptions_list = target_subscriptions.split(',')

    count = 0
    updated_subscriptions = []
    for subscription in subscriptions_list:
        if email not in subscription:
            updated_subscriptions.append(subscription)
            count += 1
    updated_subscriptions_str = ','.join(updated_subscriptions)
    
    cursor.execute("UPDATE subscriptions SET subscriptions = %s WHERE email = %s", (updated_subscriptions_str, email))
    db.commit()
    cursor.close()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
