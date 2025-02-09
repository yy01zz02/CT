

def get_cache_name(prefix, name):
    """
    Cache name constructor. Uses the same methods as django cache system
    Examples:
    *) prefix=profile.cache, name=<requestuser.id>
    *) prefix=template.cache.sidebar, name=<requestuser.id>
    """
    return '{0}.{1}'.format(
        prefix, hashlib.md5(six.text_type(name).encode('utf-8')).hexdigest()
    )


def template_source(page_pk):
    """Create cache key for page template"""
    return 'powerpages:template:{0}'.format(page_pk)


def rendered_source_for_user(page_pk, user_id):