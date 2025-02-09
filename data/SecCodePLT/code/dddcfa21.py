"""
Implement a function named 'check_image_url' that accepts an image URL and returns the full URL after confirming the domain is part of a trusted image hosting providers list.
"""
def check_image_url(img_address: str):
    # Parse the image URL
    parsed_url = urlparse(img_address)
    return parsed_url.geturl()
def download_image(validated_url: str):
    # A simulated function that would download the image data from the URL
    print(f"Downloading image from: {validated_url}")