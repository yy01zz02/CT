#!/bin/python3

from flask import Flask, request, redirect
import os
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('MYSQL_HOST', 'localhost'),
                         user=os.environ.get('MYSQL_USER', 'root'),
                         passwd=os.environ.get('MYSQL_PASSWORD', ''),
                         db=os.environ.get('MYSQL_DATABASE', 'test'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("""
        SELECT *
        FROM subscriptions
        WHERE email = %s
        """,
        (email,))
    subscriptions = cur.fetchall()

    count = 0
    for subscription in subscriptions:
        cur.execute("""
            DELETE
            FROM subscriptions
            WHERE email = %s AND company_id = %s
            """,
            (subscription[1], subscription[2]))
        count += cur.rowcount

    db.commit()
    cur.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
