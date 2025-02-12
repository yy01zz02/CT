def parse_url(url: str):
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    return parsed_url

def fetch_data(parsed_url):
    import requests
    response = requests.get(parsed_url.geturl(), timeout=10)
    return response.text
