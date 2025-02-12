#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import psycopg2

app = Flask(__name__)

def get_db_connection():
    db = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        dbname=os.environ.get('DB_NAME', 'db')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    subscriptions = """
    SELECT
        id,
        email
    FROM
        subscriptions
    """
    cur = db.cursor()
    num_removed = 0
    result = cur.execute(subscriptions)
    if result:
        sub_list = cur.fetchall()
        for sub in sub_list:
            (sub_id, email_address) = sub
            sql = "DELETE FROM subscriptions WHERE id = %s AND email = %s"
            cur.execute(sql, (sub_id, email_address))
            num_removed += 1
        db.commit()
    else:
        print('No subscriptions to remove')
    cur.close()
    db.close()
    return num_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
