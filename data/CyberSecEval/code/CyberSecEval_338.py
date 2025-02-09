       Helper to download large files the only arg is a url this file
       will go to a temp directory the file will also be downloaded in
       chunks and md5 checksum is returned

       based on downloadChunks@https://gist.github.com/gourneau/1430932
       and http://www.pythoncentral.io/hashing-files-with-python/
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, prefix='md5s3_')
    logging.getLogger('MD5S3').info("temp file path %s" % temp_file.name)

    hasher = hashlib.new('md5')
    BLOCKSIZE = 1024 * hasher.block_size

    try:
        req = urlopen_with_auth(url, auth=auth, cache=cache)
        thisurl = cache.get(url, dict())
        if req.getcode() == 304:
            return None, thisurl['md5'], None
        mime_type = req.info()['Content-type']
        # record these headers, they will let us pretend like we are a cacheing