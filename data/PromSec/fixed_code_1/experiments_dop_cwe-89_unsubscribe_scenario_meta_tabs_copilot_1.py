#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get("DB_USER"),
                         passwd=os.environ.get("DB_PASSWORD"),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from subscriptions where email=%s", (email,))
    num_subs_removed = 0
    for row in cursor.fetchall():
        cursor2 = db.cursor()
        cursor2.execute("delete from subscriptions where id=%s", (row['id'],))
        num_subs_removed += cursor2.rowcount
    db.commit()
    cursor.close()
    cursor2.close()
    db.close()
    return num_subs_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
