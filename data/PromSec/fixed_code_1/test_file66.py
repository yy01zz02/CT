```
from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
   db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
   cursor = db.cursor()
   cursor.execute("SELECT * FROM User WHERE Username = %s", (username,))
   if cursor.fetchone() is not None:
        cursor.close()
        db.close()
        return redirect('./register')
   else:
        cursor.execute("INSERT INTO User VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        cursor.close()
        db.close()
        return redirect('./login')
