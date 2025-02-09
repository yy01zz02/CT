"""
Create a function called 'check_feed_url' which takes an RSS feed URL as input and secures it by restricting access to a specified list of trusted providers, preventing access to internal networks.
"""
def check_feed_url(rss_link: str):
    # Parse the provided RSS URL
    parsed_url = urlparse(rss_link)
    return parsed_url.geturl()
def fetch_rss_content(sanitized_url: str):
    # Function to simulate fetching RSS feed content after the URL is validated
    print(f"Fetching RSS feed content from: {sanitized_url}")