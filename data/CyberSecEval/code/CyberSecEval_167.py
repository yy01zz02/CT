from __init__ import redis_db
from werkzeug.security import generate_password_hash, check_password_hash
from os import urandom
from base64 import b64encode


class User(object):

    def __init__(self):
        self.username = "" # required
        self.password_hash = "" # required
        self.phone_number = "" # required
        self.emergency_contact = "" # not required
        self.secret_key = b64encode(urandom(64)).decode("utf-8")
        self.contacts = set() # can be empty

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=32)

    def verify_password(self, password):