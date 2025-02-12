#!/bin/python3

from flask import Flask, request
import os
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host="localhost",
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db=os.environ.get('DB_NAME')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    try:
        cur.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
        count = cur.rowcount
        db.commit()
        return count
    except Exception as e:
        db.rollback()
        return 0
    finally:
        cur.close()
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email address is required.", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
