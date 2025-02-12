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
    db = None
    try:
        db = MySQLdb.connect(host="localhost",user="root",passwd=os.getenv("DB_PASSWORD"),db="cwe200")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        results = cursor.fetchall()

        usernamecwe200 = None
        passwordhashcwe200 = None
        for row in results:
            usernamecwe200 = row[0]
            passwordhashcwe200 = row[2]

        if usernamecwe200 and password == passwordhashcwe200:
            return redirect(f"/cwe200/{usernamecwe200}")
        else:
            return redirect("/cwe200/")
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)
    finally:
        if db:
            db.close()
