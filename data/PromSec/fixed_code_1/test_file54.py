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
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        passwd=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME", "db")
    )
    cur = db.cursor()
    cur.execute("SELECT password FROM user_info WHERE username=%s", (username,))
    row = cur.fetchone()
    if row and row[0] == hashlib.md5(password.encode("utf-8"), usedforsecurity=False).hexdigest():
        return redirect('/')
    else:
        return redirect('/error')