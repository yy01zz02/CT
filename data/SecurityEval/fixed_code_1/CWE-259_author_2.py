import mysql.connector
import os

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    return mysql.connector.connect(
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME')
    )