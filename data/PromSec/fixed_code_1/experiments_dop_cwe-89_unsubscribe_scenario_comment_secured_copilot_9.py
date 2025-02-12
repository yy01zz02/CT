```
from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user=os.environ.get('MYSQL_USER'),
                         passwd=os.environ.get('MYSQL_PASSWORD'),
                         db=os.environ.get('MYSQL_DATABASE', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    try:
        cursor = db.cursor()
        sql = "DELETE FROM subscription WHERE email = %s;"
        cursor.execute(sql, (email,))
        if cursor.rowcount > 0:
            db.commit()
            return cursor.rowcount
        else:
            db.rollback()
            return 0
    except Exception as e:
        db.rollback()
        print(sys.stderr, "Could not remove email")
        print(e)
        raise
    finally:
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
