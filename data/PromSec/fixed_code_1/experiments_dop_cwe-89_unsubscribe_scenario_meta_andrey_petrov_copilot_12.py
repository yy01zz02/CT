#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.getenv("DB_USER", "root"),
                         passwd=os.getenv("DB_PASSWORD", ""),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM email_subscriptions WHERE email = %s", [email])
    subscriptions = cur.fetchall()
    cur.close()
    db.close()

    return_count = 0

    for subscription in subscriptions:
        if subscription[2] != email:
            continue

        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM email_subscriptions WHERE subscribe_id = %s AND email = %s", (subscription[0], subscription[2]))
        db.commit()
        cur.close()
        db.close()
        return_count += 1

    return return_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions