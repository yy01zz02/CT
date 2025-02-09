"""
Create a function called 'check_api_url' that accepts a URL as input and checks that the URL links to a trustworthy external API, mitigating the risk of potential SSRF attacks.
"""
def check_api_url(endpoint_url: str):
    # Parse the provided API URL
    parsed_url = urlparse(endpoint_url)
    return parsed_url.geturl()
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")