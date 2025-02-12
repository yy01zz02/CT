#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT * FROM email_subscriptions WHERE EMAIL = %s"
    cursor.execute(sql, (email,))
    result = cursor.fetchall()
    if not result:
        print("We found nothing to delete")
        return 0
    print("We've found the following subscriptions to be deleted: ")
    for row in result:
        print(row)
    print("Attempting to delete them now")
    number_of_subscriptions_deleted = 0
    for row in result:
        sql = "DELETE FROM email_subscriptions WHERE EMAIL = %s AND id = %s"
        cursor.execute(sql, (row[1], row[0]))
        number_of_subscriptions_deleted += 1
    db.commit()
    db.close()
    return number_of_subscriptions_deleted

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
