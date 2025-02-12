```
#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    num_deleted = 0
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT email_address, owner_email FROM subscriptions")
    for elem in cursor.fetchall():
        if (elem["owner_email"] == email):
            cursor.execute("delete from subscriptions where owner_email = %s", (elem["email_address"],))
            num_deleted += 1
    db.commit()
    cursor.close()
    db.close()
    return num_deleted

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
