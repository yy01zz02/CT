#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
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
    cur.execute("SELECT id FROM subscriptions WHERE email = %s", (email,))
    data = cur.fetchall()
    cur.close()
    db.close()
    if not data:
        return -1
    sub_id = data[0][0]
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("UPDATE subscriptions SET email = '' WHERE id = %s", (sub_id,))
    db.commit()
    cur.close()
    db.close()
    return cur.rowcount

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
