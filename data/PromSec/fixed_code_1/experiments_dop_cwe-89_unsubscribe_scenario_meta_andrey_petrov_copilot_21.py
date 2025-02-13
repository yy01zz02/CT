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
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASS', 'root'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    number_of_subscriptions_removed = 0
    cursor = db.cursor()
    cursor.execute("SELECT id, topic, last_read_id FROM subscriptions WHERE email = %s", (email,))
    for row in cursor.fetchall():
        row_id = row[0]
        topic = row[1]
        last_read_id = row[2]
        cursor.execute("DELETE FROM subscriptions WHERE id = %s", (row_id,))
        number_of_subscriptions_removed += 1
        if last_read_id > -1:
            cursor.execute("UPDATE subscriptions SET last_read_id = %s WHERE id = %s;", (last_read_id-1, row_id))
    db.commit()
    cursor.close()
    db.close()
    return number_of_subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
