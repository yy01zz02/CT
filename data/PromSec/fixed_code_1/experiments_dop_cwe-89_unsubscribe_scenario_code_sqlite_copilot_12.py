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
    num_subscriptions_removed = 0
    cursor = db.cursor()
    cursor.execute('SELECT * FROM subscriptions')
    for row in cursor.fetchall():
        email_sub_pair = row[1].split(' ', 1)
        email_id = email_sub_pair[0]
        if (email_id == email):
            num_subscriptions_removed += 1
            cursor.execute('DELETE FROM subscriptions WHERE email=? AND label=?', [email_id, row[2]])
            db.commit()
    return num_subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
