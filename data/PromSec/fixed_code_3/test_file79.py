from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb
import re

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form.get('stock_name', '').strip()
    stock_quantity_str = request.form.get('stock_quantity', '').strip()
    username = session.get('username')

    if not username:
        return 'User not logged in', 401
    if not re.match(r'^[a-zA-Z0-9-_]+$', username):
        return 'Invalid username', 400
    if not stock_name:
        return 'Stock name is required', 400
    if not stock_quantity_str:
        return 'Stock quantity is required', 400
    if not re.match(r'^[a-zA-Z0-9-_]+$', stock_name):
        return 'Invalid stock name', 400
    try:
        stock_quantity = int(stock_quantity_str)
        if stock_quantity <= 0:
            return 'Stock quantity must be a positive integer', 400
    except ValueError:
        return 'Stock quantity must be an integer', 400

    try:
        db_user = os.environ['DB_USER']
        db_password = os.environ['DB_PASS']
        db_name = os.environ['DB_NAME']
        db = MySQLdb.connect(host=os.environ.get('DB_HOST', 'localhost'), user=db_user, passwd=db_password, db=db_name)
        cursor = db.cursor()
        sql = "INSERT INTO db_table.order_table(username, stock_name, stock_quantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, stock_name, stock_quantity))
        db.commit()
    except Exception as e:
        db.rollback()
        return f'Error: {str(e)}', 500
    finally:
        db.close()

    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    algorithm_path = os.path.normpath(os.path.join(script_dir, '../algorithm.py'))
    
    command = [
        'python3', algorithm_path,
        'buy', username, stock_name, str(stock_quantity)
    ]
    
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()
    
    return output.decode('utf-8') if proc.returncode == 0 else error.decode('utf-8')