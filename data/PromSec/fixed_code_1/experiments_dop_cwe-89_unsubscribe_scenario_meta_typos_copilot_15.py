#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', 'root')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_name = os.environ.get('DB_NAME', 'db')
    db = MySQLdb.connect(host=db_host,
                         user=db_user,
                         passwd=db_password,
                         db=db_name)
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = None
    try:
        cursor = db.cursor()
        delete_query = "DELETE FROM subscription WHERE email = %s"
        cursor.execute(delete_query, (email,))
        count = cursor.rowcount
        db.commit()
        return count
    except Exception:
        db.rollback()
        return -1
    finally:
        if cursor:
            cursor.close()
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
