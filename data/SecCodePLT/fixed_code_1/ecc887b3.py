def safe_deserialize(serialized_bytes, allowed_format="json"):
    if allowed_format == "json":
        import json
        return json.loads(serialized_bytes.decode('utf-8'))
    elif allowed_format == "xml":
        from defusedxml import ElementTree as ET
        root = ET.fromstring(serialized_bytes)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError(f"Format '{allowed_format}' is not supported.")