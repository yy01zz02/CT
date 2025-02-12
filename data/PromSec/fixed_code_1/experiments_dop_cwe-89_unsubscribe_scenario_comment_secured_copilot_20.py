```
#!/bin/python3

from flask import Flask, request, redirect
import os
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ['DB_HOST'],
                         user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASSWORD'],
                         db=os.environ['DB_NAME'])
    return db

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    dbcur = db.cursor()
    count = 0
    sql_query = "SELECT * FROM subscription WHERE subscribe_email = %s"
    dbcur.execute(sql_query, (email,))
    result_set = dbcur.fetchall()
    for row in result_set:
        subscription_id = row[0]
        sql_delete = 'DELETE FROM subscription WHERE subscription_id = %s'
        dbcur.execute(sql_delete, (subscription_id,))
        db.commit()
        count += 1
    dbcur.close()
    db.close()
    return count

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions
