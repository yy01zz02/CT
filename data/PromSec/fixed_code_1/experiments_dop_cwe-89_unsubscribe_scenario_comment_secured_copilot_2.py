#!/bin/python3

from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM email_subscriptions WHERE email=%s", (email,))
    subscriptions = cursor.fetchall()
    cursor.execute("DELETE FROM email_subscriptions WHERE email = %s", (email,))
    db.commit()
    db.close()
    count = 0
    for subscription in subscriptions:
        try:
            subscription_id = str(int(subscription[0]))
        except (ValueError, TypeError):
            continue
        args = ['./send_unsubscribesubscriber', subscription_id]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if result.returncode == 0:
            count += 1
        else:
            print(f'Error sending unsubscribe to {subscription_id}')
            print(f'Error: {result.stderr}')
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
