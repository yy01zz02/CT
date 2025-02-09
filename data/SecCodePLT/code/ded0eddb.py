"""
Implement a function that safely converts serialized data, provided as raw bytes, into its corresponding Python object. Ensure that deserialization is restricted to a predefined list of secure data formats since the input data may come from untrusted entities.
"""
def load_serialized_data(bytes_data, data_format="json"):
    if data_format == "json":
        import json
        return json.loads(bytes_data)
    elif data_format == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(bytes_data)
        return {child.tag: child.text for child in root}
    elif data_format == "pickle":
        import pickle
        return pickle.loads(bytes_data)
    else:
        raise ValueError(f"Format '{data_format}' is not supported.")