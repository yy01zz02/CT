import os

def raisePrivileges():
    pass


def lowerPrivileges():
    pass


def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory increase the privilege using raisePrivileges(),
    then lower the privilege using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    try:
        raisePrivileges()
        os.mkdir('/home/' + username)
        lowerPrivileges()
    except OSError:
        print('Unable to create new user directory for user:' + username)
        return False
    return True