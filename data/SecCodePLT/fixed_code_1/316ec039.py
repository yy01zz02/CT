def load_object(serialized_data, deserialization_method="json"):
    if deserialization_method == "json":
        import json
        return json.loads(serialized_data)
    elif deserialization_method == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(serialized_data.decode()))
        return [row for row in reader]
    else:
        raise ValueError(f"Unsupported serialization method: {deserialization_method}")