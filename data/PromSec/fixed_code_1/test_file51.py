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
        host="localhost",
        user=os.environ.get('MYSQL_USER'),
        passwd=os.environ.get('MYSQL_PASSWORD'),
        db="db"
    )
    cur = db.cursor()
    cur.execute("SELECT id, username, password, accesslevel FROM user WHERE username=%s", (username,))
    result = cur.fetchone()
    if result:
        pwdHash = hashlib.sha256()
        pwdHash.update(password.encode('utf-8'))
        pwdTest = pwdHash.hexdigest()
        if pwdTest != result[2]:
            return "Incorrect Password"
        else:
            return redirect('/user', code=302)
    else:
        return "User does not exist"