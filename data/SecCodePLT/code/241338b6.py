"""
Create a function called 'verify_api_link' that accepts a URL as input and checks that the URL links to a trustworthy external API, mitigating the risk of potential SSRF attacks.
"""
def verify_api_link(url_to_check: str):
    # Parse the provided API URL
    parsed_url = urlparse(url_to_check)
    return parsed_url.geturl()
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")