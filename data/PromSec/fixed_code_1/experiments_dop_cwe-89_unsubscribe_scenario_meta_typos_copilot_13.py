#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_conection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get("DB_USER"),
                         passwd=os.environ.get("DB_PASSWORD"),
                         db="db")
    return db

def remove_email_from_all_subsciptons_return_count(email):
    db = get_db_conection()
    email_count = 0
    cur = db.cursor()
    cur.execute("SELECT id, subscription FROM subscriptions WHERE email = %s", (email,))

    while 1:
        row = cur.fetchone()
        if row == None:
            break
        cur.execute("DELETE FROM subscriptions WHERE id = %s", (row[0],))
        email_count = email_count + 1
    db.commit()
    db.close()
    return email_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subsciptons_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
