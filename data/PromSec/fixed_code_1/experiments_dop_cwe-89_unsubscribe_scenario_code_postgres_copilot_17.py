from flask import Flask, request, redirect
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    db = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        dbname=os.environ.get('DB_NAME')
    )
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM subs_cur WHERE email = %s;", (email,))
    rows = cur.fetchall()
    if not rows:
        cur.close()
        db.close()
        return 0
    for row in rows:
        cur.execute("DELETE FROM subs WHERE id = %s", (row[0],))
    db.commit()
    cur.close()
    db.close()
    return len(rows)

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return f"You have been unsubscribed from {num_subscriptions} subscriptions."
