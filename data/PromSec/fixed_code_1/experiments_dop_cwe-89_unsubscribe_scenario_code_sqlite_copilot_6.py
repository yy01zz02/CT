from flask import Flask, request
import os
import sys
import sqlite3

app = Flask(__name__)

def get_db_connection():
    db = sqlite3.connect('emails.db')
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT id FROM subscriptions WHERE email = ?", (email,))
    results = c.fetchall()
    count = len(results)
    if count > 0:
        c.executemany("DELETE FROM subscriptions WHERE id = ?", [(result[0],) for result in results])
        db.commit()
    return count

@app.route('/email/unsubscribe_all', methods=['POST'])
def unsubscribe_all():
    email = request.form.get('email')
    if not email:
        return "Email parameter is missing", 400
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."