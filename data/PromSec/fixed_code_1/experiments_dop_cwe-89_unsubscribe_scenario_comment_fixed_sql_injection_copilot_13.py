#!/bin/python3

from flask import Flask, request
import os
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        passwd=os.environ.get('DB_PASSWORD', ''),
        db=os.environ.get('DB_NAME', 'db')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()

    c.execute("SELECT email FROM unsubscribe_subscriptions_table WHERE email = %s", (email,))
    results_list = c.fetchall()
    if not results_list:
        db.close()
        return 0

    num_removed = 0
    update_query = """
        UPDATE unsubscribe_subscriptions_table 
        SET active = 0, inactive_reason = 'No longer interested' 
        WHERE email = %s
    """
    for email_tuple in results_list:
        c.execute(update_query, (email_tuple[0],))
        num_removed += 1

    db.commit()
    db.close()
    return num_removed

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
