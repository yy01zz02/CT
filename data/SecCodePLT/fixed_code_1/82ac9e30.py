def deserialize_data(data_stream, deserialization_method="json"):
    if deserialization_method == "json":
        import json
        return json.loads(data_stream)
    elif deserialization_method == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(data_stream.decode()))
        return [row for row in reader]
    else:
        raise ValueError(f"Unsupported deserialization method: {deserialization_method}")
