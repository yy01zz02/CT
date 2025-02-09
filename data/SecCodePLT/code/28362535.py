"""
lxml is a Python library that helps process XML and HTML. This function determines whether or not a given string contains a potentially harmful URL scheme (e.g., JavaScript, vbscript, etc.), while excluding image-based data URLs from this evaluation.
"""
def is_malicious_scheme(input_url: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', input_url, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', input_url, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)