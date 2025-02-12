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
    cur = db.cursor()
    query = "SELECT id FROM subscription WHERE email=%s"
    cur.execute(query, (email,))
    subscriptions = cur.fetchall()
    count = 0
    for sub_id in subscriptions:
        delete_query = "DELETE FROM subscription WHERE id=%s"
        cur.execute(delete_query, (sub_id[0],))
        count += cur.rowcount
    db.commit()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions