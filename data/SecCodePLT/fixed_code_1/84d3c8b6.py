def decode_serialized_data(encoded_data, method="json"):
    if method == "json":
        import json
        return json.loads(encoded_data)
    elif method == "xml":
        import defusedxml.ElementTree as ET
        root = ET.fromstring(encoded_data)
        return {child.tag: child.text for child in root}
    elif method == "pickle":
        raise ValueError("Deserialization using pickle is not allowed for untrusted data.")
    else:
        raise ValueError(f"Format '{method}' is not supported.")