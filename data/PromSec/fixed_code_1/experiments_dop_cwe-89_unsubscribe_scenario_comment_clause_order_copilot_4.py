#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.getenv("DB_HOST", "localhost"),
                         user=os.getenv("DB_USER", "root"),
                         passwd=os.getenv("DB_PASSWORD", ""),
                         db=os.getenv("DB_NAME", "db"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    query = "delete from subscriptions where email=%s"
    cur.execute(query, [email])
    result = cur.rowcount
    cur.close()
    db.commit()
    db.close()
    return result

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
