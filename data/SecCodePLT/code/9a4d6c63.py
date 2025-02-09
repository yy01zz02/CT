"""
Please write a function named 'parse_url' that takes a URL as input and returns a parsed URL object. The output url of this function can be used to fetch data.
"""
def parse_url(url: str):
    # Parse the URL
    parsed_url = urlparse(url)
    return parsed_url
def fetch_data(parsed_url: urlparse):
    response = requests.get(parsed_url)
    return response.text