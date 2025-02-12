#!/bin/python3
from flask import Flask, request, redirect, session
import os
import sys
import hashlib
import MySQLdb

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        conn = MySQLdb.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            user=os.environ.get('DB_USER', 'root'),
            passwd=os.environ.get('DB_PASSWORD', ''),
            db=os.environ.get('DB_NAME', 'cwe200')
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        rows = cursor.fetchall()
        if len(rows) > 0:
            session['username'] = username
            return redirect('/session')
        else:
            return 'Incorrect username or password'
    except MySQLdb.Error:
        return 'Incorrect username or password'