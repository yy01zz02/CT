from flask import Flask, request, redirect, session
import os
import sys
import MySQLdb

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_password, db="db")
    cursor = db.cursor()
    query = "INSERT INTO `my_stocks` (user_id, stock_name, stock_quantity) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (username, stock_name, stock_quantity))
        db.commit()
        return "successfull"
    except:
        db.rollback()
        return "failure"
    finally:
        cursor.close()
        db.close()