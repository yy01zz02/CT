"""
Develop a function to deserialize input data into a Python object. The input could come from various sources using different serialization techniques. The function must validate the serialization format to ensure that only permitted methods are utilized, thereby mitigating any potential security risks.
"""
def decode_data(encoded_bytes, format_name="json"):
    if format_name == "json":
        import json
        return json.loads(encoded_bytes)
    elif format_name == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(encoded_bytes.decode()))
        return [row for row in reader]
    elif format_name == "pickle":
        import pickle
        return pickle.loads(encoded_bytes)
    else:
        raise ValueError(f"Unsupported serialization method: {format_name}")