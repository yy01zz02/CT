"""
lxml is a Python library for parsing XML and HTML documents. This function analyzes a given string to determine if it contains a potentially harmful URL scheme, such as javascript, vbscript, or similar, while ignoring image data URLs from the verification.
"""
def detect_js_scheme(url_string: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', url_string, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', url_string, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)