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
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    admin_query = "SELECT user_id FROM admin WHERE email = %s;"
    cursor = db.cursor()
    cursor.execute(admin_query, (email,))
    result = cursor.fetchone()
    actual_email = result[0] if result else None
    cursor.close()
    if not actual_email:
        return 0
    query = "SELECT user_id FROM subscriptions WHERE user_id = %s;"
    cursor = db.cursor()
    cursor.execute(query, (actual_email,))
    subscriptions = cursor.fetchall()
    initial_count = 0
    if subscriptions:
        delete_query = "DELETE FROM subscriptions WHERE user_id = %s;"
        cursor.execute(delete_query, (actual_email,))
        initial_count = cursor.rowcount
    db.commit()
    cursor.close()
    return initial_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "No email provided", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
