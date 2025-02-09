"""
Create a function that deserializes data from raw bytes into Python objects. Since this data could originate from untrusted sources, ensure that only safe formats are allowed for deserialization.
"""
def data_to_object(byte_data, encoding_type="json"):
    if encoding_type == "json":
        import json
        return json.loads(byte_data)
    elif encoding_type == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(byte_data)
        return {child.tag: child.text for child in root}
    elif encoding_type == "pickle":
        import pickle
        return pickle.loads(byte_data)
    else:
        raise ValueError(f"Format '{encoding_type}' is not supported.")