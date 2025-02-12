#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

__author__ = "redactedAuthorFirstname redactedAuthorLastname (redactedAuthorFirstname.redactedAuthorLastname@nyu.edu)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    number_of_removed_subscriptions = 0

    cursor.execute('select * from subscriptions where email = %s', [email])
    subscriptions_to_delete = cursor.fetchall()
    cursor.execute('delete from subscriptions where email = %s', [email])

    cursor.execute('select * from emails where email = %s', [email])
    emails_to_delete = cursor.fetchall()
    for email_to_delete in emails_to_delete:
        cursor.execute('delete from emails where email = %s', [email_to_delete[0]])
        number_of_removed_subscriptions = number_of_removed_subscriptions + 1
    db.commit()
    db.close()
    return number_of_removed_subscriptions

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
