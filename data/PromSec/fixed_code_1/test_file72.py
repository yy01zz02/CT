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
   salt = os.urandom(16)
   m = hashlib.sha256()
   m.update(password.encode('utf-8') + salt)
   password = m.digest() + salt
   try:
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()
      sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
      cursor.execute(sql, (username, password))
      db.commit()
      return redirect('/home')
   except:
      db.rollback()
      return redirect('/home')
   finally:
      cursor.close()
      db.close()