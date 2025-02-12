#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host=os.getenv('DB_HOST', 'localhost'),
                         user=os.getenv('DB_USER'),
                         passwd=os.getenv('DB_PASSWORD'),
                         database=os.getenv('DB_NAME'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("DELETE FROM Subscriptions WHERE email = %s ",(email,))
    db.commit()
    db.close()
    return cur.rowcount

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
