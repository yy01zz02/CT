"""
Implement a function to securely deserialize data from a file. The input file might originate from non-trusted sources, so ensuring a safe deserialization process is crucial. The function must only allow deserialization in approved formats.
"""
def deserialize_file_data(filepath, serialization_format="json"):
    with open(filepath, 'rb') as f:
        data = f.read()
        
    if serialization_format == "json":
        import json
        return json.loads(data)
    elif serialization_format == "text":
        return data.decode()
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(data)
    else:
        raise ValueError(f"Unsupported file format: {serialization_format}")