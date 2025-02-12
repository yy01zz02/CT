#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', 'root'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    all_subscriptions = db.cursor().execute("""
        SELECT * FROM subscriptions s
        LEFT JOIN users u ON s.user_id = u.id
        LEFT JOIN emails e ON s.email_id = e.id
        WHERE e.email = %s AND u.email = %s
        """, [email, email]).fetchall()
        
    db.cursor().execute("""
        DELETE s FROM subscriptions s
        LEFT JOIN users u ON s.user_id = u.id
        LEFT JOIN emails e ON s.email_id = e.id
        WHERE e.email = %s AND u.email = %s
        """, [email, email])
    db.commit()
    return len(all_subscriptions)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
