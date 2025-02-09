
def _build_gravatar_url(email, params):
    """Generate a Gravatar URL.
    
    """
    # step 1: get a hex hash of the email address
    email = email.strip().lower().encode('utf-8')
    if not EMAIL_RE.match(email):
        return ''

    email_hash = hashlib.md5(email).hexdigest()

    # step 2a: build a canonized parameters dictionary
    if not type(params).__name__ == 'dict':
        params = params.__dict__

    actual_params = {}
    default_keys = DEFAULT_PARAMS.keys()
    for key, value in params.items():
        if key in default_keys: