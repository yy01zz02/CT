"""
Create a function called 'fetch_image_url' that receives an image's URL as input and returns the final URL after ensuring the domain belongs to a list of trusted image hosting services.
"""
def fetch_image_url(url: str):
    # Parse the image URL
    parsed_url = urlparse(url)
    return parsed_url.geturl()
def download_image(valid_url: str):
    # A simulated function that would download the image data from the URL
    print(f"Downloading image from: {valid_url}")