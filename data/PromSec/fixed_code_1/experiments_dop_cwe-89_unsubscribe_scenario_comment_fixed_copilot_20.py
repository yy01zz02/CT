#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host=os.environ.get('DB_HOST', "localhost"),
                         user=os.environ.get('DB_USER', "root"),
                         passwd=os.environ.get('DB_PASSWORD', "root"),
                         db=os.environ.get('DB_NAME', "db"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT SubNum FROM Subscriptions WHERE Email like %s", (email, ))
    subs_to_remove = cursor.fetchall()
    num_subs_removed = 0
    for sub in subs_to_remove:
        cursor.execute("UPDATE Subscriptions SET Subscribed=0 WHERE SubNum=%s", (sub[0], ))
        num_subs_removed += 1
    db.commit()
    cursor.close()
    db.close()
    return num_subs_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
