#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.getenv("DB_HOST", "localhost"),
                         user=os.getenv("DB_USER", "root"),
                         passwd=os.getenv("DB_PASSWORD", "root"),
                         db=os.getenv("DB_NAME", "db"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        if not result:
            return 0
        uid = result[0]

        cursor.execute("DELETE FROM subscription WHERE user_id = %s AND email = %s", (uid, email))
        db.commit()
        number_removed = cursor.rowcount
    except Exception as e:
        db.rollback()
        number_removed = 0
    finally:
        cursor.close()
        db.close()

    return number_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
