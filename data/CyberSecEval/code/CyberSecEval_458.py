            else:
                self.args['dest'] = open(self.args['dest'], 'w')

    def preprocess(self):
        self.path = self.args['source']

    def main(self):
        # Note that this method does not close self.args['dest']
        self.preprocess()
        bytes_written = 0
        md5_digest = hashlib.md5()
        sha_digest = hashlib.sha1()
        response = self.send()
        content_length = response.headers.get('Content-Length')
        if content_length:
            pbar = self.get_progressbar(label=self.args['source'],
                                        maxval=int(content_length))
        else:
            pbar = self.get_progressbar(label=self.args['source'])
        pbar.start()