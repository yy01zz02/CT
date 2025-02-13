def load_serial_data(f_path, f_format="json"):
    with open(f_path, 'rb') as f:
        content = f.read()
        
    if f_format == "json":
        import json
        return json.loads(content)
    elif f_format == "text":
        return content.decode()
    else:
        raise ValueError(f"Unsupported file format: {f_format}")
