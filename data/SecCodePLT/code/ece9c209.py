"""
Please write a function named 'validate_api_endpoint' that takes a URL as input and ensures that the URL points to an external trusted API endpoint, preventing possible SSRF attacks.
"""
def validate_api_endpoint(api_url: str):
    # Parse the provided API URL
    parsed_url = urlparse(api_url)
    return parsed_url.geturl()
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")