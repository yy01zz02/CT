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

    db = MySQLdb.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db=os.environ.get('DB_NAME')
    )
    cur = db.cursor()

    cur.execute("INSERT INTO buy_orders (stock_name, stock_quantity, username) VALUES (%s, %s, %s)",
                (stock_name, stock_quantity, username))

    db.commit()
    db.close()

    return redirect('/')