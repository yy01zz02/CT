#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.getenv("DB_HOST", "localhost"),
                         user=os.getenv("DB_USER"),
                         passwd=os.getenv("DB_PASSWORD"),
                         db=os.getenv("DB_NAME", "db"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()

    sql = """DELETE FROM all_subscriptions
             WHERE email = %s
          """

    try:
        cursor.execute(sql, (email,))
        db.commit()
    except Exception as e:
        print("ERROR: " + str(e), file=sys.stderr)
        db.rollback()
        db.close()
        return 0
    db.close()
    return cursor.rowcount

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
