def deserialize_data(input_data, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(input_data)
    elif serialization_format == "xml":
        import defusedxml.ElementTree as ET
        root = ET.fromstring(input_data)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError(f"Format '{serialization_format}' is not supported.")