    @type  url: basestring

    @return: Local path of the url
    @rtype:  basestring
    """
    url = urlparse.unquote(url)
    local_path = settings.STATIC_ROOT + os.path.normpath(url[len(settings.STATIC_URL):])
    return local_path

# `buffer` is needed since hashlib apparently isn't unicode safe
hexhash = lambda s: hashlib.md5(buffer(s)).hexdigest()

def new_rendered_path(orig_path, width, height, ext=None):
    """
    Builds a new rendered path based on the original path, width, and height.
    It takes a hash of the original path to prevent users from accidentally 
    (or purposely) overwritting other's rendered thumbnails.

    This isn't perfect: we are assuming that the original file's conents never 
    changes, which is the django default.  We could make this function more