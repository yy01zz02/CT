#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get("DB_USER"),
                         passwd=os.environ.get("DB_PASSWORD"),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()
    count = 0
    c.execute("SELECT topic FROM subscriptions")
    data = c.fetchall()
    for row in data:
        c.execute("DELETE FROM subscriptions "
                  " WHERE email = %s "
                  "   AND topic = %s", (email, row[0]))
        count += c.rowcount
    print('Removed ' + str(count) + ' subscriptions.')
    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
