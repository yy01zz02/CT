from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   confirm_password = request.form['confirm_password']
   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()
   cur.execute("SELECT * FROM users WHERE username = %s", (username,))
   row = cur.fetchall()
   if not row:
      try:
         cur.execute("INSERT INTO users(username, pw_hash) VALUES(%s, %s)", (username, pw_hash))
         cnx.commit()
         message = "You have successfully registered"
         cur.close()
         cnx.close()
         return message
      except:
         cnx.rollback()
         message = "Registration Failed"
         cur.close()
         cnx.close()
         return message
   else:
      message = "Username already exists"
      cur.close()
      cnx.close()
      return message
