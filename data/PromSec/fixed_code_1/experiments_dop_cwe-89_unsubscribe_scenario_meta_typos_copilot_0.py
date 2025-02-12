from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get("MYSQL_HOST", "localhost"),
                         user=os.environ.get("MYSQL_USER", "root"),
                         passwd=os.environ.get("MYSQL_PASSWORD", ""),
                         db=os.environ.get("MYSQL_DB", "db"))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    count = 0
    try:
        sql = "DELETE FROM subscriptions WHERE email = %s"
        cursor.execute(sql, (email,))
        db.commit()
        count = cursor.rowcount
        print(str(count) + " subscriptions removed")
    except Exception as e:
        print(f"Unable to delete subscriptions: {str(e)}")
        db.rollback()
    finally:
        db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
