#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', 'root'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    """remove the given email from all subscriptions in the database
    and return the number of subscriptions removed"""
    db = get_db_connection()

    try:
        cursor = db.cursor()
        removing_email_query = "DELETE FROM subscriptions WHERE email = %s;"
        cursor.execute(removing_email_query, (email,))
    except:
        db.rollback()
        print(sys.exc_info()[0])
        exit()
    else:
        db.commit()

    db.close()
    return cursor.rowcount


@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    """URL handler to remove a user from all subscriptions"""
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
