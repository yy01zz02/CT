#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get("DB_HOST", "localhost"),
                         user=os.environ.get("DB_USER", "root"),
                         passwd=os.environ.get("DB_PASSWORD", "root"),
                         db=os.environ.get("DB_NAME", "db"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    total_deleted = 0
    
    cursor.execute("SELECT id_subscribed FROM subscribed WHERE email_address = %s", (email,))
    subscribed_ids = cursor.fetchall()
    
    delete_query = "DELETE FROM subscribed WHERE id_subscribed = %s"
    
    for row in subscribed_ids:
        id_subscribed = row[0]
        cursor.execute(delete_query, (id_subscribed,))
        total_deleted += cursor.rowcount
    
    db.commit()
    db.close()
    return total_deleted

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
