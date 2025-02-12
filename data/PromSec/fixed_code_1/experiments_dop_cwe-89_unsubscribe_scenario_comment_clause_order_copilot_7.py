#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT sub FROM subscription")
    rows = cur.fetchall()
    db.close()
    count = 0
    for row in rows:
        if email in row[0]:
            count += 1
            db = get_db_connection()
            db.begin()
            cur = db.cursor()
            try:
                new_sub = row[0].replace(email, "")
                cur.execute("UPDATE subscription SET sub=%s WHERE sub=%s", (new_sub, row[0]))
                db.commit()
            except:
                print("Error: unable to update data")
                db.rollback()
            db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
