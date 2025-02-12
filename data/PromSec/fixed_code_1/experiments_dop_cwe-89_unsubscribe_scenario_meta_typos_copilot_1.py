#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_conection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', 'root'),
                         db="db")
    return db

def remove_email_from_all_subsciptons_return_count(email):
    db = get_db_conection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM subscriptions")
    subscriptions = cursor.fetchall()
    count = 0
    for subscription in subscriptions:
        cursor.execute("DELETE FROM subscriptions WHERE email=%s AND username=%s", (email, subscription[0]))
        db.commit()
        count += 1
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subsciptons_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
