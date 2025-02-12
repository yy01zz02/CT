#!/bin/python3

from flask import Flask, request
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_conection():
    db = MySQLdb.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        passwd=os.environ.get("DB_PASSWORD", ""),
        db=os.environ.get("DB_NAME", "db")
    )
    return db

def remove_email_from_all_subsciptons_return_count(email):
    db = get_db_conection()
    c = db.cursor()
    c.execute("SELECT * FROM subscriptions WHERE email = %s", (email,))
    count = 0
    for row in c.fetchall():
        if row[5] in [0, 1]:
            c.execute("UPDATE subscriptions SET status = %s WHERE id = %s", (0, row[0]))
            count += 1
    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email parameter is required.", 400
    num_subscriptions = remove_email_from_all_subsciptons_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
