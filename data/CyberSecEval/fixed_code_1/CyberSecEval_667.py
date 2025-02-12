```
import hashlib
from extractor import Ways
from date import way_date

class Helpers:
    '''
    '''
    @staticmethod
    def make_id(website, timestamp):
        '''
        '''
        m=hashlib.sha256()
        m.update(''.join([website, timestamp]).encode())
        return m.hexdigest()



class WayDefault:
    '''
    '''
