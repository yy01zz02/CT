from flask import Flask, request
import os
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        passwd=os.environ.get("DB_PASSWORD", ""),
        db=os.environ.get("DB_NAME", "db")
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    stmt = "DELETE FROM subscription WHERE email = %s"
    cursor.execute(stmt, (email,))
    num_deleted = cursor.rowcount
    db.commit()
    cursor.close()
    db.close()
    return num_deleted

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
