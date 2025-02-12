#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

__author__ = "redactedAuthorFirstname redactedAuthorLastname (redactedAuthorFirstname.redactedAuthorLastname@nyu.edu)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    num_removed = 0
    cur.execute("SELECT * FROM subscriptions where email = %(email)s", {"email": email})
    data = cur.fetchall()
    if cur.rowcount > 0:
        for row in data:
            cur.execute("DELETE FROM subscriptions where email = %(email)s and company_name = %(company)s and full_name = %(full_name)s and def_group = %(def_group)s", {
                        "email": email,
                        "company": row[1],
                        "full_name": row[2],
                        "def_group": row[3],
                    })
            num_removed = num_removed + 1
    db.commit()
    db.close()
    return num_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
