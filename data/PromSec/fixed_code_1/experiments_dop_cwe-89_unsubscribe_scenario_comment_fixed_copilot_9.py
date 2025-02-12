#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user=os.environ.get('DB_USER', 'root'),
        passwd=os.environ.get('DB_PASS', 'root'),
        db="db"
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    result = 0
    try: 
        cur.execute("SELECT * FROM subscriptions WHERE email = %s", (email,))
        subscriptions = cur.fetchall()
        for subscription in subscriptions:
            sub_id = subscription[0]
            cur.execute("DELETE FROM subs WHERE id = %s", (sub_id,))
            result += 1
    except Exception as e:
        print(f"Unable to delete subscriptions: {e}")
    finally:
        db.commit()
        cur.close()
        db.close()
    return result

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
