from multiprocessing import Lock
from hashlib import sha256

global bountyList
global bountyLock
global bountyPath
global masterKey
bountyList = []
bountyLock = Lock()
bounty_path = "data" + os.sep + "bounties.pickle"
masterKey = rsa.PublicKey(*pickle.load(open("master_public_key.pickle", "rb")))


def getUTC():
    from calendar import timegm
    from time import gmtime
    return timegm(gmtime())


class Bounty(object):