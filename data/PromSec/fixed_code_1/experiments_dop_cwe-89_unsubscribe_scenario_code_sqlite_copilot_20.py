#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import sqlite3

app = Flask(__name__)

def get_db_connection():
    db = sqlite3.connect('emails.db')
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.execute("SELECT email, source FROM subscriptions")
    subscriptions = cursor.fetchall()
    cursor.close()

    count = 0
    for (email_to_remove, source) in subscriptions:
        if email in email_to_remove:
            remove_email_from_subscription(email_to_remove, source)
            count += 1

    db.commit()
    db.close()

    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
