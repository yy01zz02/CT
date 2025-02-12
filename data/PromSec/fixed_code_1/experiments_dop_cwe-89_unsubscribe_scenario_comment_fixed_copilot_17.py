#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor(buffered=True)
    
    check_user_sql = "SELECT * FROM users WHERE email = %s"
    cursor.execute(check_user_sql, (email,))
    if cursor.rowcount > 0:
        print("User exists in database")
    else:
        print("User not found in database")
    
    delete_sql = "DELETE FROM subscriptions WHERE email = %s"
    cursor.execute(delete_sql, (email,))
    db.commit()
    
    deleted_count = cursor.rowcount
    cursor.close()
    db.close()
    
    return deleted_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
