#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', 'root'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT * FROM subscriptions WHERE email = %s"
    try:
        cursor.execute(sql, (email,))
        data = cursor.fetchall()
        num_subscriptions = len(data)
        if num_subscriptions == 0:
            db.close()
            return num_subscriptions
    except MySQLdb.Error as e:
        print(e)
        db.close()
        return -1
    
    for sub in data:
        sub_id = sub[0]
        sql_c = "SELECT * FROM request WHERE sub_id = %s"
        try:
            cursor.execute(sql_c, (sub_id,))
            data_c = cursor.fetchall()
            if data_c:
                for req in data_c:
                    email_id = req[1]
                    sql_r = "DELETE FROM request WHERE id = %s"
                    try:
                        cursor.execute(sql_r, (email_id,))
                        db.commit()
                    except MySQLdb.Error as e:
                        print(e)
                        db.rollback()
            sql_s = "DELETE FROM subscriptions WHERE id = %s"
            try:
                cursor.execute(sql_s, (sub_id,))
                db.commit()
            except MySQLdb.Error as e:
                print(e)
                db.rollback()
        except MySQLdb.Error as e:
            print(e)
            db.close()
            return -1
    db.close()
    return num_subscriptions

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
