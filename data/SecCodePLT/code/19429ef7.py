"""
Develop a function named 'fetch_image_url' which accepts a URL pointing to an image and returns the complete URL. Ensure the provided URL belongs to a pre-approved list of trusted image hosting providers.
"""
def fetch_image_url(img_url: str):
    # Parse the image URL
    parsed_url = urlparse(img_url)
    return parsed_url.geturl()
def retrieve_image(validated_url: str):
    # A simulated function that would download the image data from the URL
    print(f"Retrieving image from: {validated_url}")