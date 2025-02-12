#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import psycopg2

app = Flask(__name__)

def get_db_connection():
    db = psycopg2.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         password=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    db_cursor = db.cursor()
    sub_count = 0
    db_cursor.execute("SELECT count(*) FROM subscriptions WHERE email=%s", (email,))
    sub_count = db_cursor.fetchone()[0]
    db_cursor.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
    db.commit()
    db.close()
    return sub_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
