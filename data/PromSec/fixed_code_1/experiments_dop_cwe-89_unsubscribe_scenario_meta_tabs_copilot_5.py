#!/usr/bin/env python3

from flask import Flask, request
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db=os.environ.get('DB_NAME', 'db')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
    db.commit()

    num_rows_deleted = cursor.rowcount

    cursor.close()
    db.close()

    return num_rows_deleted

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email address is required.", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
