def load_serialized_data(filepath, data_format="json"):
    with open(filepath, 'rb') as f:
        content = f.read()
        
    if data_format == "json":
        import json
        return json.loads(content)
    elif data_format == "text":
        return content.decode()
    else:
        raise ValueError(f"Unsupported file format: {data_format}")
