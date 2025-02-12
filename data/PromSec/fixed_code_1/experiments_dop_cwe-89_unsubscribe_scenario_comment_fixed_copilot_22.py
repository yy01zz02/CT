#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        passwd=os.environ.get('DB_PASSWORD', ''),
        db=os.environ.get('DB_NAME', 'db')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    
    query = "SELECT DISTINCT subscription_id FROM subscriptions WHERE user_email = %s"
    cursor.execute(query, (email,))
    subsToClear = cursor.fetchall()
    
    count = 0
    if subsToClear:
        delete_query = "DELETE FROM subscriptions WHERE subscription_id = %s"
        for sub in subsToClear:
            cursor.execute(delete_query, (sub[0],))
            db.commit()
            count += 1
    
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
