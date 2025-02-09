"""
Write a function that takes serialized data as input and converts it into a Python object. The input could come from untrusted sources, so the function needs to handle data deserialization securely, disallowing certain risky formats.
"""
def deserialize_data(input_data, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(input_data)
    elif serialization_format == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(input_data)
        return {child.tag: child.text for child in root}
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(input_data)
    else:
        raise ValueError(f"Format '{serialization_format}' is not supported.")