import json
from urllib.parse import urlparse
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ('http', 'https'):
        raise ValueError("Invalid URL scheme")
    response = request.urlopen(url)
    data = json.loads(response.read())
    return data