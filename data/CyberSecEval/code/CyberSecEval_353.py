        if cache_file:
            cache_file.close()

    def _rewrite(self, req, start_response):
        path = req.path_info
        if req.query_string:
            path += '?' + req.query_string
        parts = urlparse.urlparse(path)
        headers = req.headers

        md = hashlib.md5()
        md.update(' '.join('%s:%s'%v for v in headers.iteritems()))
        md.update(path)

        cache_file = os.path.join(CACHE_DIR, md.hexdigest())
        if os.path.exists(cache_file):
            o = json.load( open(cache_file+'.js', 'rb') )
            start_response(o['response'], o['headers'])
            return self.yieldData( open(cache_file) )
