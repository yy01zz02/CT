            print 'Warning: Running without RPC'
        
        if new_streams is None:
            new_streams = []
            
        streams = self.streams + new_streams

        for url in itertools.cycle(streams):
            print url
            self.check_feed(url)
            time.sleep(random.randint(*self.wait_range))

    def check_feed(self, url):
        for fail_count in itertools.count():
            try:
                datad = feedparser.parse(url)
            except:
                print 'Parse error for', url
                time.sleep(min(2 ** fail_count, self.max_error_wait))
            else: