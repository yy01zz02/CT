def deserialize_data(raw_data, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(raw_data)
    elif serialization_format == "xml":
        import defusedxml.ElementTree as ET
        root = ET.fromstring(raw_data)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError(f"Format '{serialization_format}' is not supported.")