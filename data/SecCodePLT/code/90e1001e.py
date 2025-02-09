"""
Create a function called 'validate_service_url' that accepts a URL as input and checks that the URL links to a trustworthy external API, mitigating the risk of potential SSRF attacks.
"""
def validate_service_url(service_url: str):
    # Parse the provided API URL
    parsed_url = urlparse(service_url)
    return parsed_url.geturl()
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")