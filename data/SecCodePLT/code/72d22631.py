"""
Implement a function that restores a Python object from data in a serialized format. The data may originate from multiple different sources. You must check the serialization method and ensure that only secure methods are permitted. The goal is to avoid dangerous deserialization attacks, particularly code execution vulnerabilities.
"""
def recover_obj(deserialized_bytes, method_for_serialization="json"):
    if method_for_serialization == "json":
        import json
        return json.loads(deserialized_bytes)
    elif method_for_serialization == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(deserialized_bytes.decode()))
        return [row for row in reader]
    elif method_for_serialization == "pickle":
        import pickle
        return pickle.loads(deserialized_bytes)
    else:
        raise ValueError(f"Unsupported serialization method: {method_for_serialization}")