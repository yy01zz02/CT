#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        passwd=os.environ.get("DB_PASSWORD", "root"),
        database=os.environ.get("DB_NAME", "db")
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    try:
        cursor = db.cursor()

        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        if not result:
            return 0
        user_id = result[0]

        cursor.execute("SELECT id FROM subscriptions WHERE user_id = %s", (user_id,))
        subscriptions_ids = cursor.fetchall()

        count = 0
        for subscription_id in subscriptions_ids:
            cursor.execute("DELETE FROM subscriptions WHERE user_id = %s AND id = %s", (user_id, subscription_id[0]))
            count += 1
        db.commit()
    finally:
        db.close()

    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
