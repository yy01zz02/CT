from flask import Flask, request, redirect, session
import os
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', 'db')

    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_password, db=db_name)
    cursor = db.cursor()
    cursor.execute("INSERT INTO orders (username, stock_name, stock_quantity, buy_price) VALUES (%s, %s, %s, 10000)", 
                   (username, stock_name, stock_quantity))
    db.commit()
    return redirect('/')
