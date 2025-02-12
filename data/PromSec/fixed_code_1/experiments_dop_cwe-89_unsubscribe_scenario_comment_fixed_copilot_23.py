from flask import Flask, request, redirect
import os
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host="localhost",
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db="db")
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    r = get_all_subscriptions_by_email(email)
    subscription_ids = [subscription[0] for subscription in r]
    count = 0

    for subscription_id in subscription_ids:
        subscription = access_subscription(subscription_id, db)
        subscription[0][2] = remove_email(subscription[0][2], email)
        if(subscription[0][2] is None or subscription[0][2]==''):
            delete_subscription(subscription_id, db)
            count += 1
        else:
            modify_subscription(subscription[0][0], subscription[0][1], subscription[0][2], db)
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
