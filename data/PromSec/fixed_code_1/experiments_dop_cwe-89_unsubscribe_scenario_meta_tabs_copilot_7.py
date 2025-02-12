#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
	db = MySQLdb.connect(host="localhost",
						 user=os.environ.get('DB_USER'),
						 passwd=os.environ.get('DB_PASSWORD'),
						 db=os.environ.get('DB_NAME'))
	return db

def remove_email_from_all_subscriptions_return_count(email):
	db = get_db_connection()
	cursor = db.cursor()

	subscriptions = get_all_subscriptions_for_email_address(email)
	for subscription in subscriptions:
		cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email, ))

	cursor.execute("""DELETE FROM subscriptions WHERE email in (SELECT DISTINCT email FROM subscriptions)""")

	db.commit()

	return subscription_count()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
	email = request.args.get('email')
	num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
	return "You have been unsubscribed from %s subscriptions." % num_subscriptions
