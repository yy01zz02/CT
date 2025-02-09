        """Finishes this response, ending the HTTP request."""
        assert not self._finished
        if chunk is not None:
            self.write(chunk)    # 特别注意, 这里的关键调用

        # Automatically support ETags and add the Content-Length header if
        # we have not flushed any content yet.
        if not self._headers_written:
            if (self._status_code == 200 and self.request.method == "GET" and
                        "Etag" not in self._headers):
                hasher = hashlib.sha1()
                for part in self._write_buffer:
                    hasher.update(part)

                etag = '"%s"' % hasher.hexdigest()
                inm = self.request.headers.get("If-None-Match")

                if inm and inm.find(etag) != -1:
                    self._write_buffer = []
                    self.set_status(304)