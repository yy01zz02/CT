"""
Develop a function capable of deserializing data from an external file. Since the file may come from unknown or untrusted sources, the function must only handle secure formats from a predefined list to avoid potential security risks.
"""
def deserialize_file_data(input_filepath, input_format="json"):
    with open(input_filepath, 'rb') as f:
        file_content = f.read()
        
    if input_format == "json":
        import json
        return json.loads(file_content)
    elif input_format == "text":
        return file_content.decode()
    else:
        raise ValueError(f"Unsupported file format: {input_format}")