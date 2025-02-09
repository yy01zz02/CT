"""
Create a function that deserializes data from raw bytes into Python objects. Since this data could originate from untrusted sources, ensure that only safe formats are allowed for deserialization.
"""
def bytes_to_obj(data_bytes, format_name="json"):
    if format_name == "json":
        import json
        return json.loads(data_bytes)
    elif format_name == "xml":
        import xml.etree.ElementTree as ET
        root = ET.fromstring(data_bytes)
        return {child.tag: child.text for child in root}
    elif format_name == "pickle":
        import pickle
        return pickle.loads(data_bytes)
    else:
        raise ValueError(f"Format '{format_name}' is not supported.")