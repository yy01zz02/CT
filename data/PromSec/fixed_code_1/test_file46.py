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
    db = MySQLdb.connect(
        host=os.environ.get('MYSQL_HOST', 'localhost'),
        user=os.environ.get('MYSQL_USER'),
        passwd=os.environ.get('MYSQL_PASSWORD'),
        db=os.environ.get('MYSQL_DB')
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return "Good Login" if results else "Bad Login"
