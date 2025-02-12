#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    sql_delete_subscription = "DELETE FROM tbl_subscription WHERE email = %s"
    cursor.execute(sql_delete_subscription, (email,))
    db.commit()
    cursor.execute("SELECT COUNT(*) FROM tbl_subscription WHERE email = %s", (email,))
    count = int(cursor.fetchone()[0])
    cursor.close()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email parameter is required", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
