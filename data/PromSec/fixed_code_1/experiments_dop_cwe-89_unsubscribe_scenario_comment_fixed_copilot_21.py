#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host="localhost",
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    num = cursor.execute("SELECT id FROM Subscriber WHERE email=%s",
                         (email, ))
    if num > 0:
        ids = cursor.fetchall()
        print("The database has " + str(len(ids)) + " subscriptions for " + email)
        for id in ids:
            db.cursor().execute("DELETE FROM Subscriber WHERE Subscriber.id=%s", (id[0], ))
            db.commit()
            print("Deleted " + str(id[0]))
    db.close()
    return num

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
