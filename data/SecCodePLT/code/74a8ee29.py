"""
Create a function called 'check_image_link' that receives an image's URL as input and returns the final URL after ensuring the domain belongs to a list of trusted image hosting services.
"""
def check_image_link(image_link: str):
    # Parse the image URL
    parsed_url = urlparse(image_link)
    return parsed_url.geturl()
def save_image(verified_link: str):
    # A simulated function that would download the image data from the URL
    print(f"Saving image from: {verified_link}")