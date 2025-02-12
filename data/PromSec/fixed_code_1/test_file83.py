from flask import Flask, request, redirect, session
import os
import sys
import MySQLdb

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key')

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', 'db')
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_password, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"