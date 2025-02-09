import base64
import MySQLdb
import os


def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    db = MySQLdb.connect(
        host="localhost",
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db="test"
    )
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE userid = %s", (userid,))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return base64.b64decode(result[0]) == password