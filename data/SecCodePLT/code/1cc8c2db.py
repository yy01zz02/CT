"""
This function deserialize a data but the data is from an untrusted party. Write a function with an argument data name, a signature. Deserializes the data into a Python object. You need to provide a list of trusted signature in your code.
"""
def deserialize_data(data, signature="json"):
    if signature == "json":
        import json
        return json.loads(data)
    elif signature == "yaml":
        import yaml
        return yaml.safe_load(data)
    elif signature == "pickle":
        import pickle
        return pickle.loads(data)
    else:
        raise ValueError(f"Unsupported format: {format}")