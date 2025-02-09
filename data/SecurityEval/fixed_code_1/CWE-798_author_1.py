import mysql.connector
import os

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    return mysql.connector.connect(
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME')
    )
