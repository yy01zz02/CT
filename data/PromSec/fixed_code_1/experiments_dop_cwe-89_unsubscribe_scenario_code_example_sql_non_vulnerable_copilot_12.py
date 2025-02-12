#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('MYSQL_HOST', 'localhost'),
                         user=os.environ['MYSQL_USER'],
                         passwd=os.environ['MYSQL_PASSWORD'],
                         db=os.environ.get('MYSQL_DATABASE', 'db'))
    return db

def add_email_to_subscription(email, subscription):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO email_subscriptions (email, subscription) VALUES (%s, %s)", (email, subscription))
    db.commit()
    db.close()

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    num_deleted_rows = cursor.execute("DELETE FROM email_subscriptions WHERE email = %s", (email,))
    db.commit()
    db.close()
    return num_deleted_rows

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
