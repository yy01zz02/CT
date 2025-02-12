#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('MYSQL_USER', 'root'),
                         passwd=os.environ.get('MYSQL_PASSWORD', ''),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("""
        SELECT subscription_id
        FROM subscription
        WHERE subscription_type_id IN (SELECT subscription_type_id
                                        FROM subscription_type
                                        WHERE subscription_type_name = 'email')
        AND email = %s
    """, [email])
    if not cur.rowcount:
        return 0
    subscriptions = cur.fetchall()
    subscriptions_remove = dict()
    for subscription in subscriptions:
        subscriptions_remove[subscription[0]] = subscription[1]
    cur.execute("""
        DELETE
        FROM subscription
        WHERE subscription_type_id IN (SELECT subscription_type_id
                                        FROM subscription_type
                                        WHERE subscription_type_name = 'email')
        AND email = %s
    """, [email])
    db.commit()
    db.close()
    return len(subscriptions_remove)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
