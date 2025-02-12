from flask import Flask, request
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT id FROM email WHERE email = %s", (email,))
    result = cur.fetchone()
    if not result:
        cur.close()
        db.close()
        return 0
    email_id = result[0]

    cur.execute("SELECT id FROM job WHERE email_id = %s", (email_id,))
    job_result = cur.fetchone()
    if not job_result:
        cur.close()
        db.close()
        return 0
    id_of_job = job_result[0]

    cur.execute("UPDATE subscription SET email = 0 WHERE subscription.job_id = %s", (id_of_job,))
    subscription_count = cur.rowcount
    cur.execute("UPDATE job SET email = 0 WHERE job.id = %s", (id_of_job,))
    db.commit()
    cur.close()
    db.close()
    return subscription_count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
