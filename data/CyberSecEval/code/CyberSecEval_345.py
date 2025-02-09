        """
        fields = ("Host", "Sec-Websocket-Key", "Sec-Websocket-Version")
        if not all(map(lambda f: self.request.headers.get(f), fields)):
            raise ValueError("Missing/Invalid WebSocket headers")

    @staticmethod
    def compute_accept_value(key):
        """Computes the value for the Sec-WebSocket-Accept header,
        given the value for Sec-WebSocket-Key.
        """
        sha1 = hashlib.sha1()
        sha1.update(utf8(key))
        sha1.update(b"258EAFA5-E914-47DA-95CA-C5AB0DC85B11")  # Magic value
        return native_str(base64.b64encode(sha1.digest()))

    def _challenge_response(self):
        return WebSocketProtocol13.compute_accept_value(
            self.request.headers.get("Sec-Websocket-Key"))

    def _accept_connection(self):