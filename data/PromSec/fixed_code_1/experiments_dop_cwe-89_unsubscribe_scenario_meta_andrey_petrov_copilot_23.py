#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"

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
    email_ls = email.split(',')
    count = 0
    for row in cursor.execute("SELECT * FROM subscriptions"):
        if (email_ls[0] in row[1].split(',') and email_ls[1] in row[2].split(',')):
            new_subscription = row[1].replace(email_ls[0], '')
            new_subscription = new_subscription.replace(email_ls[1], '')
            cursor.execute("UPDATE subscriptions SET subscriptions = %s WHERE id = %s", (new_subscription, row[0]))
            count += 1
    cursor.execute("ALTER TABLE subscriptions DROP subscriptions")
    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
