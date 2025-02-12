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
    c.execute("DELETE FROM sub_emails WHERE email=?", (email,))
    count = c.rowcount
    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
