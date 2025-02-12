#!/bin/python3

from flask import Flask, request, redirect, session
import os
import sys
import MySQLdb

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'),
                         user=os.environ.get('DB_USER', 'root'),
                         passwd=os.environ.get('DB_PASSWORD', ''),
                         db=os.environ.get('DB_NAME', 'db'))
    return db

def insert_user_message_in_db(username, message):
    db = get_db_connection()
    c = db.cursor()
    query = "INSERT INTO messages (username, content) VALUES (%s, %s)"
    c.execute(query, (username, message))
    db.commit()
    db.close()

@app.route('/post', methods=['POST'])
def post():
    username = session['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')
