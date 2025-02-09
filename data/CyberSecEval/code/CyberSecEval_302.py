    def getPackage(self):
        # One application has only one package name
        return self.packageNames[0]

    def getHashes(self, block_size=2 ** 8):
        """
        Calculate MD5,SHA-1, SHA-256
        hashes of APK input file
        """
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        f = open(self.filename, 'rb')
        while True:
            data = f.read(block_size)
            if not data:
                break

            md5.update(data)
            sha1.update(data)