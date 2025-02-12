from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASS', ''),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * from subscriptions")
    subscriptions = cur.fetchall()
    delete_subscriptions = []
    for subscription in subscriptions:
        cur.execute(
            "UPDATE subscriptions SET emails = REPLACE(emails, %s, '') WHERE subscription_id = %s",
            (email, subscription[0])
        )
        if cur.rowcount > 0:
            delete_subscriptions.append(subscription[0])
    db.commit()
    db.close()
    return len(delete_subscriptions)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
