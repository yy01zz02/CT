#!/bin/python3
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
    try:
        db = MySQLdb.connect(host="localhost",
                     user="cwe",
                     passwd=os.environ.get("DB_PASSWORD"),
                     db="cwe")
        cursor = db.cursor()
        cursor.execute("SELECT password FROM registered_users WHERE username=%s", (username,))
        data = cursor.fetchall()
        db.close()
    except Exception as e:
        print(e)
        return redirect('/internal_server_error')
    if (len(data) == 0):
        return redirect('/cant_login')
    else:
        h = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if (data[0][0] == h):
            return redirect('/success')
        else:
            return redirect('/cant_login')
