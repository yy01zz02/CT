#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    affected_rows = 0
    cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
    user_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM subscriptions WHERE user_id=%s", (user_id,))
    subscriptions = cursor.fetchall()
    for subscription in subscriptions:
        cursor.execute("DELETE FROM subscriptions WHERE user_id=%s AND id=%s", (user_id, subscription[0]))
        affected_rows += cursor.rowcount
    db.commit()
    db.close()
    return affected_rows

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
