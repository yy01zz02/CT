#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.getenv('DB_HOST', 'localhost'),
                         user=os.getenv('DB_USER', 'root'),
                         passwd=os.getenv('DB_PASSWORD', ''),
                         db=os.getenv('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()

    query = "DELETE FROM cwe_digest_subscriptions WHERE email=%s;"
    cursor.execute(query, (email,))
    db.commit()
    num_digest_removed = cursor.rowcount

    query = "DELETE FROM cwe_regular_subscriptions WHERE email=%s;"
    cursor.execute(query, (email,))
    db.commit()
    num_regular_removed = cursor.rowcount

    cursor.close()
    db.close()

    return {"digest": num_digest_removed, "regular": num_regular_removed}

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    if not email:
        return "Email parameter is required.", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    total = num_subscriptions['digest'] + num_subscriptions['regular']
    return "You have been unsubscribed from %s subscriptions." % total
