#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    numToRemove = 0

    sql = "UPDATE subscriptions SET userEmail=NULL WHERE userEmail = %s;"
    try:
        cursor.execute(sql, [email])
        numToRemove += cursor.rowcount
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Unexpected error:", sys.exc_info()[1])

    db.commit()
    db.close()
    return numToRemove

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
