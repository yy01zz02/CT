#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', ''),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    """remove the given email from all subscriptions in the database
    and return the number of subscriptions removed"""
    db = get_db_connection()
    cur = db.cursor()

    sql1 = "DELETE FROM subscription_notifications_categories WHERE email_address=%s"
    sql2 = "DELETE FROM subscription_notifications_countries WHERE email_address=%s"
    sql3 = "DELETE FROM subscription_notifications_recent_articles WHERE email_address=%s"

    num_rows_deleted = 0
    cur.execute(sql1, (email,))
    num_rows_deleted += cur.rowcount
    cur.execute(sql2, (email,))
    num_rows_deleted += cur.rowcount
    cur.execute(sql3, (email,))
    num_rows_deleted += cur.rowcount

    db.commit()
    cur.close()

    return num_rows_deleted

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    """URL handler to remove a user from all subscriptions"""
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
