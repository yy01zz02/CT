#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host="localhost",
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT email FROM subscriptions")
    subscriptions = cur.fetchall()
    removed = 0
    for subscription in subscriptions:
        if(subscription[0] == email):
            cur.execute("DELETE FROM subscriptions WHERE email = %s", [email,])
            removed += 1
    db.commit()
    db.close()
    return removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
