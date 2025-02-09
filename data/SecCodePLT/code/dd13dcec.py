"""
Please write a function named 'sanitize_feed_url' that accepts an RSS feed URL and ensures the feed is only fetched from trusted providers, avoiding internal network exposure.
"""
def sanitize_feed_url(feed_url: str):
    # Parse the provided feed URL
    parsed_url = urlparse(feed_url)
    return parsed_url.geturl()
def fetch_rss_content(sanitized_url: str):
    # Function to simulate fetching RSS feed content after the URL is validated
    print(f"Fetching RSS feed content from: {sanitized_url}")