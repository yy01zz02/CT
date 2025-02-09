
        for b in d.splitter.bridges:
            # china blocks some transports
            for pt in b.transports:
                if random.choice(xrange(2)) > 0:
                    key = "%s:%s" % (pt.address, pt.port)
                    b.blockingCountries[key] = set(['cn'])
            for address, portlist in b.or_addresses.items():
                # china blocks some transports
                for port in portlist:
                    if random.choice(xrange(2)) > 0:
                        key = "%s:%s" % (address, port)
                        b.blockingCountries[key] = set(['cn'])
            key = "%s:%s" % (b.ip, b.orport)
            b.blockingCountries[key] = set(['cn'])

        # we probably will get at least one bridge back!
        # it's pretty unlikely to lose a coin flip 250 times in a row
        for i in xrange(5):
            b = d.getBridgesForIP(randomIPString(), "x", 1,