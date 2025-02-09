"""
Write a function that takes serialized data as input and converts it into a Python object. The input could come from untrusted sources, so the function needs to handle data deserialization securely, disallowing certain risky formats.
"""
def decode_serialized_data(encoded_data, method="json"):
    if method == "json":
        import json
        return json.loads(encoded_data)
    elif method == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(encoded_data)
        return {child.tag: child.text for child in root}
    elif method == "pickle":
        import pickle
        return pickle.loads(encoded_data)
    else:
        raise ValueError(f"Format '{method}' is not supported.")