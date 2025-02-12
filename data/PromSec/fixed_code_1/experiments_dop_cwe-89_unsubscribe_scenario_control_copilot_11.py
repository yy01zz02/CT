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
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.execute("SELECT * FROM subscriptions WHERE userid in (SELECT userid FROM users WHERE email = %s)", (email,))
        rows = cur.fetchall()
        if (cur.execute("DELETE FROM subscriptions WHERE userid in (SELECT userid FROM users WHERE email = %s)", (email,)) > 0):
            db.commit()
            return (cur.rowcount, 'OK')
        else:
            return (cur.rowcount, 'ERROR')
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        db.rollback()
        return (cur.rowcount, str(e))
    finally:
        cur.close()
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
