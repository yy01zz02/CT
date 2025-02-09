import json

class Payload(object):
    pass

def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    return json.dumps(payload.__dict__).encode()
