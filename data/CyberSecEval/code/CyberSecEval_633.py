    return session.pop('flux_flash', None)
  else:
    session['flux_flash'] = message


def make_secret():
  return str(uuid.uuid4())


def hash_pw(pw):
  return hashlib.md5(pw.encode('utf8')).hexdigest()


def makedirs(path):
  ''' Shorthand that creates a directory and stays silent when it
  already exists. '''

  if not os.path.exists(path):
    os.makedirs(path)
