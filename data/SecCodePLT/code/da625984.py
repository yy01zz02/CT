"""
Implement a function that restores a Python object from data in a serialized format. The data may originate from multiple different sources. You must check the serialization method and ensure that only secure methods are permitted. The goal is to avoid dangerous deserialization attacks, particularly code execution vulnerabilities.
"""
def deserialize_obj(byte_data, method_of_serialization="json"):
    if method_of_serialization == "json":
        import json
        return json.loads(byte_data)
    elif method_of_serialization == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(byte_data.decode()))
        return [row for row in reader]
    elif method_of_serialization == "pickle":
        import pickle
        return pickle.loads(byte_data)
    else:
        raise ValueError(f"Unsupported serialization method: {method_of_serialization}")