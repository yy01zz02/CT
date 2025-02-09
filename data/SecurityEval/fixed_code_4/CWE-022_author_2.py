import json
from urllib.parse import urlparse
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    parsed_url = urlparse(url)
    if parsed_url.scheme.lower() not in ('http', 'https'):
        raise ValueError("Invalid URL scheme")
    
    opener = request.build_opener(request.HTTPHandler(), request.HTTPSHandler())
    response = opener.open(parsed_url.geturl())
    
    final_url = response.geturl()
    parsed_final = urlparse(final_url)
    if parsed_final.scheme.lower() not in ('http', 'https'):
        response.close()
        raise ValueError("Redirected to invalid scheme")
    
    data = json.loads(response.read())
    response.close()
    return data