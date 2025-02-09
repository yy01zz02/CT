import mysql.connector
import os

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(
        host="localhost",
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD')
    )

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user
