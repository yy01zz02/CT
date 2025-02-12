from util import app
import hashlib
import os

phase2_url = '/phase2-%s/' % os.environ.get('PHASE2_TOKEN')
admin_password = os.environ.get('ADMIN_PASSWORD', '')
admin_hash = hashlib.sha256(admin_password.encode('utf-8')).hexdigest()
session_key = 'sessionkey'
admin_session_key = 'adminsessionkey'


def init_data(redis):
    redis.set('user:test:password', hashlib.sha256(b'test').hexdigest())
    redis.set('user:admin:password', admin_hash)
    redis.set('user:test:1', 'Buy groceries')
    redis.set('user:test:2', 'Clean the patio')