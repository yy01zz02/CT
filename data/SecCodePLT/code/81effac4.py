"""
Write a function named 'check_api_link' that accepts a URL representing an API endpoint and ensures that it directs to an external, trusted API, protecting against possible Server-Side Request Forgery (SSRF) vulnerabilities.
"""
def check_api_link(api_link: str):
    # Parse the provided API URL
    parsed_url = urlparse(api_link)
    return parsed_url.geturl()
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")