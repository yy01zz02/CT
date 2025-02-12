#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    removed_count = 0
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
        removed_count = cursor.rowcount
        db.commit()
    except MySQLdb.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        db.rollback()
    finally:
        cursor.close()
        db.close()
    return removed_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email parameter is required", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
