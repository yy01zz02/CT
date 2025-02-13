def read_serialized_file(file_path, file_format="json"):
    with open(file_path, 'rb') as f:
        data = f.read()
        
    if file_format == "json":
        import json
        return json.loads(data)
    elif file_format == "text":
        return data.decode()
    else:
        raise ValueError(f"Unsupported file format: {file_format}")