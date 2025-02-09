

    """ INTERNAL METHODS FOLLOW """

    def _get_new_timestamp(self):
        """ Returns a fresh timestamp in proper format """
        return time.strftime('%Y-%m-%dT%H:%M:%S%z')

    def _get_hash(self):
        """ Form and return the parameters hash for the API request """
        md5 = hashlib.md5()
        md5.update(self._json_string.encode('utf-8'))
        return md5.hexdigest()


    def _get_message(self):
        """ Return the message in the format which is used to create signature of the request """
        message = "\n".join([
            self._method,
            self._get_hash(),