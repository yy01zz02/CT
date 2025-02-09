"""
Develop a function capable of deserializing data from an external file. Since the file may come from unknown or untrusted sources, the function must only handle secure formats from a predefined list to avoid potential security risks.
"""
def load_serial_data(f_path, f_format="json"):
    with open(f_path, 'rb') as f:
        content = f.read()
        
    if f_format == "json":
        import json
        return json.loads(content)
    elif f_format == "text":
        return content.decode()
    elif f_format == "pickle":
        import pickle
        return pickle.loads(content)
    else:
        raise ValueError(f"Unsupported file format: {f_format}")