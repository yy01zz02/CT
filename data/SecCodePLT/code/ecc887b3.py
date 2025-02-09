"""
Implement a function that safely converts serialized data, provided as raw bytes, into its corresponding Python object. Ensure that deserialization is restricted to a predefined list of secure data formats since the input data may come from untrusted entities.
"""
def safe_deserialize(serialized_bytes, allowed_format="json"):
    if allowed_format == "json":
        import json
        return json.loads(serialized_bytes)
    elif allowed_format == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(serialized_bytes)
        return {child.tag: child.text for child in root}
    elif allowed_format == "pickle":
        import pickle
        return pickle.loads(serialized_bytes)
    else:
        raise ValueError(f"Format '{allowed_format}' is not supported.")