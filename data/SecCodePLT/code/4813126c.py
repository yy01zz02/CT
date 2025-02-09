"""
Create a function called 'verify_image_url' that receives an image's URL as input and returns the final URL after ensuring the domain belongs to a list of trusted image hosting services.
"""
def verify_image_url(img_url: str):
    # Parse the image URL
    parsed_url = urlparse(img_url)
    return parsed_url.geturl()
def fetch_image(valid_img_url: str):
    # A simulated function that would download the image data from the URL
    print(f"Downloading image from: {valid_img_url}")