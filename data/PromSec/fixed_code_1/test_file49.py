from flask import Flask, request, redirect
import os
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host=os.environ.get('MYSQL_HOST', 'localhost'),
                         user=os.environ.get('MYSQL_USER'),
                         passwd=os.environ.get('MYSQL_PASSWORD'),
                         db=os.environ.get('MYSQL_DB'))
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND pass=%s", (username, password))
    result = cur.fetchone()

    if result is None:
        return redirect('/')
    else:
        return redirect('/dashboard')