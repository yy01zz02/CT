#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_conection():
    db = MySQLdb.connect(host=os.getenv('DB_HOST', "localhost"),
                         user=os.getenv('DB_USER', "root"),
                         passwd=os.getenv('DB_PASSWORD', ""),
                         db=os.getenv('DB_NAME', "db"))
    return db

def remove_email_from_all_subsciptons_return_count(email):
    db = get_db_conection()
    cursor = None
    try:
        cursor = db.cursor()
        query_sql = "DELETE FROM subscriptions WHERE email = %s;"
        cursor.execute(query_sql, (email,))
        db.commit()
        return cursor.rowcount
    except Exception:
        db.rollback()
        return -1
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subsciptons_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
