from urlparse import urlparse, parse_qs
from mopidy import backend
from mopidy.models import SearchResult, Track, Album, Artist
import pykka
import pafy
import requests
import unicodedata
from mopidy_youtube import logger

yt_api_endpoint = 'https://www.googleapis.com/youtube/v3/'
yt_key = 'AIzaSyAl1Xq9DwdE_KD4AtPaE4EJl3WZe2zCqg4'


def resolve_track(track, stream=False):
    logger.debug("Resolving Youtube for track '%s'", track)
    if hasattr(track, 'uri'):
        return resolve_url(track.comment, stream)
    else:
        return resolve_url(track.split('.')[-1], stream)
