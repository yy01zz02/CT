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
    c = db.cursor()
    c.execute('SELECT email FROM subscriptions WHERE email = ?;', (email,))
    rows = c.fetchall()
    if len(rows) == 0:
        db.close()
        return 0
    else:
        c.execute('DELETE FROM subscriptions WHERE email = ?;', (email,))
        db.commit()
        db.close()
        return len(rows)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
