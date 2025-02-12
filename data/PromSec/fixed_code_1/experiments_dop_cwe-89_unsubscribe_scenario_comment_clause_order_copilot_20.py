#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get("DB_USER", "root"),
                         passwd=os.environ.get("DB_PASSWORD", ""),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    sql_statement = "SELECT id, date, s_email, r_email FROM subscriptions WHERE s_email=%s"
    cursor.execute(sql_statement, (email,))
    rows = cursor.fetchall()
    cursor.close()

    count = 0
    for row in rows:
        count += 1
        remove_subscription_and_notify_recipient(db, row[0], row[1], row[2], row[3], email)
    
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
