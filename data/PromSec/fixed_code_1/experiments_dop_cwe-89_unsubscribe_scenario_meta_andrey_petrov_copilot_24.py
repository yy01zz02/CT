#!/bin/python3

from flask import Flask, request
import os
import sys
import MySQLdb

__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', ''),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    db.autocommit(False)
    cur = db.cursor()

    try:
        query = """UPDATE subscriptions 
                   SET is_active=0, last_modified=UTC_TIMESTAMP() 
                   WHERE email=%s;"""
        cur.execute(query, (email,))
        count = cur.rowcount
        db.commit()
    except Exception:
        db.rollback()
        count = 0
    finally:
        cur.close()
        db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email parameter is required.", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
