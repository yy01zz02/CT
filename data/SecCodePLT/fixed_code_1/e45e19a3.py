def deserialize_data(input_data, data_type="json"):
    if data_type == "json":
        import json
        return json.loads(input_data)
    elif data_type == "xml":
        from defusedxml import ElementTree as ET
        root = ET.fromstring(input_data)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError(f"Format '{data_type}' is not supported.")
