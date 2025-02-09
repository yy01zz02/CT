"""
The Python library lxml is used to handle XML and HTML content. The objective of this function is to determine whether a given string contains a risky URL scheme, such as javascript, vbscript, or other similar schemes, excluding valid image data URLs from the check.
"""
def has_script_scheme(url: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', url, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', url, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)