from flask import Flask, request
import os
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ["DB_USER"],
        passwd=os.environ["DB_PASSWORD"],
        database=os.environ.get("DB_NAME", "db")
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    emails_cur = db.cursor()
    subscriptions_cur = db.cursor()
    result = 0
    email_exists = False
    try:
        emails_cur.execute("SELECT email FROM users WHERE email = %s", (email,))
        if emails_cur.rowcount > 0:
            email_exists = True
            emails_cur.execute("DELETE FROM users WHERE email = %s", (email,))
            subscriptions_cur.execute("SELECT count(*) FROM subscriptions WHERE user_email = %s", (email,))
            result = subscriptions_cur.fetchone()[0]
            subscriptions_cur.execute("DELETE FROM subscriptions WHERE user_email = %s", (email,))
            db.commit()
    except Exception as e:
        db.rollback()
    finally:
        emails_cur.close()
        subscriptions_cur.close()
        db.close()
    return (result, email_exists)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    count, exists = remove_email_from_all_subscriptions_return_count(email)
    if exists:
        return f"You have been unsubscribed from {count} subscriptions."
    return "No subscriptions found for this email."
