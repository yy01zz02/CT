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
    subscriptions_removed_num = 0
    cursor = db.cursor()
    cursor.execute("SELECT * FROM subscriptions WHERE type = 1")
    subscriptions = cursor.fetchall()
    for subscription in subscriptions:
        email_list = subscription[4].split(',')
        if email in email_list:
            email_list.remove(email)
            if len(email_list) == 1:
                email_list.append(email)
            email_str = ",".join(email_list)
            cursor.execute("UPDATE subscriptions SET email_list=%s WHERE id=%s", (email_str, subscription[0]))
            subscriptions_removed_num += 1
    db.commit()
    cursor.close()
    return subscriptions_removed_num

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
