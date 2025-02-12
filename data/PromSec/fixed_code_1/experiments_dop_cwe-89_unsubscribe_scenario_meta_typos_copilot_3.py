#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_conection():
    db = MySQLdb.connect(host=os.environ.get("DB_HOST", "localhost"),
                         user=os.environ.get("DB_USER"),
                         passwd=os.environ.get("DB_PASSWORD"),
                         db=os.environ.get("DB_NAME", "db"))
    return db

def remove_email_from_all_subsciptons_return_count(email):
    db = get_db_conection()
    cur = db.cursor()
    cur.execute("SELECT count(*) FROM subscriptions WHERE user_email = %s;", (email,))
    count = cur.fetchone()[0]
    cur.execute("DELETE FROM subscriptions WHERE user_email = %s", (email,))
    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subsciptons_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
