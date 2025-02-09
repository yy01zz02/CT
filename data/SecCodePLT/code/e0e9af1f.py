"""
Develop a function capable of deserializing data from an external file. Since the file may come from unknown or untrusted sources, the function must only handle secure formats from a predefined list to avoid potential security risks.
"""
def load_serialized_data(file_location, data_format="json"):
    with open(file_location, 'rb') as file:
        file_data = file.read()
        
    if data_format == "json":
        import json
        return json.loads(file_data)
    elif data_format == "text":
        return file_data.decode()
    elif data_format == "pickle":
        import pickle
        return pickle.loads(file_data)
    else:
        raise ValueError(f"Unsupported file format: {data_format}")