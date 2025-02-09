import os

def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    return password == os.environ.get('ADMIN_PASSWORD')
