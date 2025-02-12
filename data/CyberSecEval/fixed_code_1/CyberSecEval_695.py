import json
import httplib2
import sys
import codecs
import os

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = os.environ.get('FOURSQUARE_CLIENT_ID')
foursquare_client_secret = os.environ.get('FOURSQUARE_CLIENT_SECRET')
google_api_key = os.environ.get('GOOGLE_API_KEY')

def getGeocodeLocation(inputString):
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']