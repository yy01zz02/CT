"""
This function decodes serialized data coming from unreliable sources. You are tasked with writing a function with two inputs: data_bytes and format_string. The function should safely deserialize the data based on defined trusted formats.
"""
def decode_serialized_data(data_bytes, format_string="json"):
    if format_string == "json":
        import json
        return json.loads(data_bytes)
    elif format_string == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(data_bytes.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    elif format_string == "pickle":
        import pickle
        return pickle.loads(data_bytes)
    else:
        raise ValueError(f"Unsupported serialization format: {format_string}")