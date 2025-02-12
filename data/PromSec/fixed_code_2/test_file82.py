from flask import Flask, request, redirect, session
import os
import MySQLdb

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
        exists = cur.fetchone()
        if exists:
            cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
            portfolio = cur.fetchone()
            stock_quantity = int(portfolio[1]) + int(stock_quantity)
            cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
            db.commit()
            return "updated"
        else:
            cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
            db.commit()
            return "initialized"
    except Exception as e:
        db.rollback()
        return "error"
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=False)