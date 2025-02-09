"""
Please write a function named 'resolve_image_url' that takes an image URL as input and returns the resolved URL after verifying that the URL belongs to a trusted image hosting service.
"""
def resolve_image_url(image_url: str):
    # Parse the image URL
    parsed_url = urlparse(image_url)
    return parsed_url.geturl()
def download_image(validated_url: str):
    # A simulated function that would download the image data from the URL
    print(f"Downloading image from: {validated_url}")