    def _make_signature(self):
        """
        生成请求签名
        """

        # 40位随机字符
        # nonce = "".join([str(randint(0, 9)) for _ in range(40)])
        nonce = "4103657107305326101203516108016101205331"

        sha1 = "{0}:{1}:{2}".format(self.key, self.realm, self.secret).encode("utf-8")
        sha1 = hashlib.sha1(sha1).hexdigest()
        sha2 = "{0}:{1}".format(self.http_method, self.uri).encode("utf-8")
        sha2 = hashlib.sha1(sha2).hexdigest()

        signature = "{0}:{1}:{2}".format(sha1, nonce, sha2).encode("utf-8")
        signature = hashlib.sha1(signature).hexdigest()

        ret = collections.namedtuple("signature_return", "signature nonce")
        ret.signature = signature
        ret.nonce = nonce