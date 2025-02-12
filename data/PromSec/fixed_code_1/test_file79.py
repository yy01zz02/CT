from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

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
        'buy', username, stock_name, stock_quantity
    ]
    
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()
    
    return output.decode('utf-8') if proc.returncode == 0 else error.decode('utf-8')