"""
Implement a function that safely converts serialized data, provided as raw bytes, into its corresponding Python object. Ensure that deserialization is restricted to a predefined list of secure data formats since the input data may come from untrusted entities.
"""
def deserialize_data(raw_data, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(raw_data)
    elif serialization_format == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(raw_data)
        return {child.tag: child.text for child in root}
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(raw_data)
    else:
        raise ValueError(f"Format '{serialization_format}' is not supported.")