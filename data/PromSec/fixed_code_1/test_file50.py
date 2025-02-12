Here is the fixed code:

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
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db=os.environ.get('DB_NAME')
    )
    cursor = db.cursor()
    cursor.execute("SELECT password FROM user WHERE username = %s", (username,))
    login_results = cursor.fetchall()
    db.close()
    if not login_results:
        return "Wrong Password"
    for row in login_results:
        if row[0] == hashlib.sha256(password.encode()).hexdigest():
            return "Login Success"
    return "Wrong Username"
