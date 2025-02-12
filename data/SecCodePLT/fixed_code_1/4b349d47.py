To fix the vulnerabilities, we need to address both the XML and pickle-related issues. For XML, we replace the vulnerable `xml.etree.ElementTree` with the secure `defusedxml` library. The unsafe `pickle` deserialization is removed entirely to prevent arbitrary code execution. JSON processing remains safe when using standard parsers without object hooks.

def convert_to_object(serialized_data, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(serialized_data)
    elif format_type == "xml":
        from defusedxml.ElementTree import fromstring
        root = fromstring(serialized_data)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError(f"Format '{format_type}' is not supported.")
