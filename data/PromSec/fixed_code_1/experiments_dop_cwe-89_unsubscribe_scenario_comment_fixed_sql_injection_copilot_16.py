#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

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
    cur.execute("SELECT * FROM subscriptions LEFT OUTER JOIN users ON "
             "subscriptions.user_id=users.id LEFT OUTER JOIN users_in_groups ON"
             " subscriptions.user_id=users_in_groups.user_id WHERE email=%s ORDER BY"
             " subscriptions.id DESC", [email])
    data = cur.fetchall()
    cur.close()
    db.close()
    print("[+] Removing subscriptions and users for %s" % email)
    errcnt = 0
    for row in data:
        print("[+] Removing subscription %d" % row[0])
        errcnt += remove_subscription(row[0])
        errcnt += remove_user_from_group(email, row[5])

    return errcnt

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
