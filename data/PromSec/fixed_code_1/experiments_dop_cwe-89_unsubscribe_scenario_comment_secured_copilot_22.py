#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.getenv('DB_USER', 'root'),
                         passwd=os.getenv('DB_PASSWORD', 'root'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()
    query = "SELECT count(*), sum(length(email_id)) FROM subscriptions WHERE email_id LIKE %s;"
    c.execute(query, ('%' + email + '%',))
    result = c.fetchall()[0]
    count = result[0]
    if (count == 0):
        db.close()
        return 0
    else:
        select_query = "SELECT email FROM subscriptions WHERE email_id LIKE %s;"
        c.execute(select_query, ('%' + email + '%',))
        email_result = c.fetchall()
        delete_query = "DELETE FROM subscriptions WHERE email_id LIKE %s;"
        c.execute(delete_query, ('%' + email + '%',))
        db.commit()
        db.close()
        return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
