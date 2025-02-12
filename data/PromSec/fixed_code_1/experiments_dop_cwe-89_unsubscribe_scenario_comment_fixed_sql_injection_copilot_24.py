#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASS'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    sql = """UPDATE subscriptions_settings s
        SET `num_subscriptions_removed` = 
        (
            SELECT COUNT(*) 
            FROM subscriptions 
            WHERE s.`email` = %s
            AND (
                SELECT COUNT(*)
                FROM subscriptions
                WHERE email = %s
                AND subscriptions.`id` <> s.`id`
            ) = 0
        )
        WHERE s.`email` = %s"""
    sql_vars = (email, email, email)
    cursor.execute(sql, sql_vars)
    db.commit()
    db.close()
    return cursor.rowcount

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
