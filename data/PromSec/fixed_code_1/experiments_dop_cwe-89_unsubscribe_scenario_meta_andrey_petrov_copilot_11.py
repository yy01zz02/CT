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
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT id FROM email_subscriptions WHERE email_subscriptions.email = %s", (email,))
    result = cur.fetchall()
    if len(result) == 0:
        return 0
    else:
        ids_to_remove = [str(result[0][0])]
        for id in ids_to_remove:
            cur.execute("DELETE FROM subscription WHERE subscription.id = %s", (id,))
        db.commit()
        db.close()
        return len(ids_to_remove)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
