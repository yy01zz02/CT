from flask import Flask, request, redirect, session
import os
import sys
import hashlib
import MySQLdb

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')
    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass, db=db_name)
    cursor = db.cursor()
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    try:
        cursor.execute(sql, (username, password))
        results = cursor.fetchall()
        if results:
            row = results[0]
            session['id'] = row[0]
            session['Role'] = row[1]
            return redirect('/dashboard')
        return redirect('/login')
    except Exception:
        return redirect('/login')
    finally:
        cursor.close()
        db.close()