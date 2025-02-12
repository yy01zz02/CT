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
						 db="db")
	return db

def remove_email_from_all_subscriptions_return_count(email):
	db = get_db_connection()
	cur = db.cursor()
	cur.execute("SELECT id,subscribed,username,did FROM subscriptions")
	num_rows = cur.rowcount
	print("Rows returned: "+str(num_rows))
	if num_rows == 0:
		db.close()
		return 0
	count = 0
	for row in cur.fetchall():
		if row[1] == email:
			cur.execute("UPDATE subscriptions SET subscribed=%s WHERE id=%s",(row[2],str(row[0])))
			count += 1
	db.commit()
	db.close()
	return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
	email = request.args.get('email')
	num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
	return "You have been unsubscribed from %s subscriptions." % num_subscriptions
