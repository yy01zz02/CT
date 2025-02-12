#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host=os.environ.get("DB_HOST", "localhost"),
                         user=os.environ.get("DB_USER"),
                         passwd=os.environ.get("DB_PASSWORD"),
                         db=os.environ.get("DB_NAME"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    query = ("SELECT * FROM subscriptions WHERE email = %s")
    cursor.execute(query, (email,))
    results = cursor.fetchall()
    cursor.close()
    db.close()
    if len(results) > 0:
        for result in results:
            sub_id = result[0]
            email = result[4]
            remove_database_entry_email(sub_id, email)
        return str(len(results))
    return "0"

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
