import secrets
import string


def generateRandomString(length):
    '''
    Return an unpredictable random string that has only ASCII letters with a fixed size equals to length.
    '''
    return ''.join(secrets.choice(string.ascii_letters) for i in range(length))
