#!/bin/python3

from flask import Flask, request
import os
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        passwd=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME")
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    if not email:
        return 0
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE subscription SET email = %s WHERE email = %s", (' ', email))
        count = cursor.rowcount
        db.commit()
        return count
    except Exception:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
