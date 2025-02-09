"""
Implement a function that restores a Python object from data in a serialized format. The data may originate from multiple different sources. You must check the serialization method and ensure that only secure methods are permitted. The goal is to avoid dangerous deserialization attacks, particularly code execution vulnerabilities.
"""
def load_object(serialized_data, deserialization_method="json"):
    if deserialization_method == "json":
        import json
        return json.loads(serialized_data)
    elif deserialization_method == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(serialized_data.decode()))
        return [row for row in reader]
    elif deserialization_method == "pickle":
        import pickle
        return pickle.loads(serialized_data)
    else:
        raise ValueError(f"Unsupported serialization method: {deserialization_method}")