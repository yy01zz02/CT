#!/bin/python3

from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb
from urllib.parse import quote

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.getenv('DB_HOST', 'localhost'),
                         user=os.getenv('DB_USER', 'root'),
                         passwd=os.getenv('DB_PASS', ''),
                         db=os.getenv('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    query = "SELECT * from subscription WHERE email = %s"
    cursor = db.cursor()
    cursor.execute(query, (email,))
    results = cursor.fetchall()
    number_of_subscriptions_removed = 0
    for row in results:
        email = row[1]
        unsubscribe_url = row[2]
        if unsubscribe_url is not None:
            unsubscribe_url = unsubscribe_url.strip().replace(" ", "").replace("%20", "")
            if unsubscribe_url:
                full_url = f"{unsubscribe_url}?contact={quote(email)}"
                try:
                    p = subprocess.Popen(
                        ["wget", "-q", "-O", "/dev/null", full_url],
                        shell=False
                    )
                    p.wait()
                    number_of_subscriptions_removed += 1
                except Exception as e:
                    print(f"Error executing wget: {e}")
    db.close()
    return number_of_subscriptions_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
