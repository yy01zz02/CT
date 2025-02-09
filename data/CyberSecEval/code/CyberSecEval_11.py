            try:
                portlist.add(b.or_addresses[address])
            except KeyError:
                pass
            finally:
                b.or_addresses[address] = portlist

    if transports:
        for i in xrange(0,8):
            b.transports.append(bridgedb.Bridges.PluggableTransport(b,
                random.choice(["obfs", "obfs2", "pt1"]),
                randomIP(), randomPort()))

    return b

def fake16Bridge(orport=8080, running=True, stable=True):
    nn = "bridge-%s"%random.randrange(0,1000000)
    ip = random16IP()
    fp = "".join([random.choice("0123456789ABCDEF") for _ in xrange(40)])
    b = bridgedb.Bridges.Bridge(nn,ip,orport,fingerprint=fp)  