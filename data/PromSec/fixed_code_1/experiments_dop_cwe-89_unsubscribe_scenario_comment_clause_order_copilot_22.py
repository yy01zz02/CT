#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb
import requests

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    num_subs_removed = 0 
    cursor.execute("SELECT cwe_89_callback_url FROM callback_urls")
    for callback in cursor.fetchall():
        new_callback = callback[0].replace("__REPLACE_EMAIL__", email)
        try:
            r = requests.delete(new_callback, timeout=10)
            if r.status_code == 204:
                num_subs_removed += 1
        except Exception as e:
            print(f"Error unsubscribing: {str(e)}")
            print("callback: " + str(new_callback))
    return num_subs_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
