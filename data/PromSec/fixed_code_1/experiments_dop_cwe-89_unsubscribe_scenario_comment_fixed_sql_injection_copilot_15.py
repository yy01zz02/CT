```
from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASS'],
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT * FROM subscriptions")
    if c.rowcount > 0:
        c.execute("SELECT * FROM subscriptions")
        subscriptions = list()
        for row in c.fetchall():
            subscriptions.append(row[1])
        c.execute("SELECT * FROM subscriptions")
        new_subscriptions = list()
        for row in c.fetchall():
            new_tuple = ()
            new_tuple += (row[1],)
            if email != row[1]:
                new_subscriptions.append(new_tuple)
        c.execute("SELECT COUNT(*) FROM subscriptions")
        if c.fetchone()[0] == 0:
            pass
        else:
            db = get_db_connection()
            c = db.cursor()
            c.executemany("INSERT INTO subscriptions VALUES(%s, %s)", new_subscriptions)
            db.commit()
    return c.rowcount

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
