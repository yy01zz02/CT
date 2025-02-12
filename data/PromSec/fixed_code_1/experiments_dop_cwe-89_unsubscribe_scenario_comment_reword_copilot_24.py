#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        passwd=os.environ.get('DB_PASSWORD', ''),
        db=os.environ.get('DB_NAME', 'db')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    total = 0

    try:
        cursor.execute("DELETE FROM notification WHERE email = %s", (email,))
        total += cursor.rowcount
        cursor.execute("DELETE FROM notification WHERE to_from IN (SELECT email FROM user WHERE email = %s)", (email,))
        total += cursor.rowcount
        cursor.execute("DELETE FROM subscription WHERE email = %s", (email,))
        total += cursor.rowcount
        cursor.execute("DELETE FROM subscription WHERE to_from IN (SELECT email FROM notification WHERE email = %s)", (email,))
        total += cursor.rowcount
        cursor.execute("DELETE FROM user WHERE email = %s", (email,))
        total += cursor.rowcount
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cursor.close()
        db.close()

    return total

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
