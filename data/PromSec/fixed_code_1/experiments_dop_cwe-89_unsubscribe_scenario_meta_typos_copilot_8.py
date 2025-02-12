from flask import Flask, request
import os
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')
    if not all([db_user, db_password, db_name]):
        raise ValueError("Missing database environment variables")
    return MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT id FROM subscriptions WHERE email = %s", (email,))
        subscriptions = cursor.fetchall()
        count = 0
        for (subscription_id,) in subscriptions:
            cursor.execute("DELETE FROM subscriptions WHERE id = %s", (subscription_id,))
            count += 1
        db.commit()
        return count
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return 0
    finally:
        db.close()

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
