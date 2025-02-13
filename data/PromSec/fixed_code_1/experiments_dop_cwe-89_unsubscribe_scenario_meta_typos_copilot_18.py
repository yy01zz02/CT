from flask import Flask, request, redirect
import os
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db="db")
    return db

def remove_email_from_all_subsciptons_return_count(email):
    db = get_db_connection()
    db_cursor = db.cursor()
    db_cursor.execute("SELECT id FROM subcription WHERE email=%s", (email,))
    all_email_subscriptions = db_cursor.fetchall()
    subscribe_count=0
    for subscription in all_email_subscriptions:
        db_cursor.execute("SELECT COUNT(1) FROM subcription WHERE id=%s", (subscription[0],))
        if db_cursor.fetchone()[0] == 0:
            db_cursor.execute("DELETE FROM subcription WHERE id=%s", (subscription[0],))
            db.commit()
            subscribe_count += 1
    db.close()
    return subscribe_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subsciptons_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
