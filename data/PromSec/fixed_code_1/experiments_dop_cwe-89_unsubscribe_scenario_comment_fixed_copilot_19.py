#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    count = 0
    if db.is_connected():
        if is_email_valid(email):
            cur = db.cursor()
            cur.execute("SELECT id FROM subscriptions WHERE email = %s", [email])
            rows = cur.fetchall()
            for row in rows:
                cur = db.cursor()
                cur.execute("DELETE FROM subscriptions WHERE id = %s", [row[0]])
                count += 1
            db.commit()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
