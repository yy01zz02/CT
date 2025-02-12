```
#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    count = 0

    try:
        cursor.execute("""
            SELECT list_of_emails FROM subscriptions WHERE email=%s
            """, (email,))
        rows = cursor.fetchall()
        for row in rows:
            old_list_of_emails = row[0]
            new_list_of_emails = old_list_of_emails.replace(email, '')
            cursor.execute("""
                UPDATE subscriptions SET list_of_emails=%s
                WHERE email=%s
                """, (new_list_of_emails, email))
            count += 1

        cursor.execute("""
            DELETE FROM subscriptions WHERE email=%s
            """, (email,))

        db.commit()
        return count
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        db.rollback()
    finally:
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
