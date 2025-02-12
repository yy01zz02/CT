def load_serialized_data(bytes_data, data_format="json"):
    if data_format == "json":
        import json
        return json.loads(bytes_data)
    elif data_format == "xml":
        import defusedxml.ElementTree as ET
        root = ET.fromstring(bytes_data)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError(f"Format '{data_format}' is not supported.")