"""
The goal of this function is to deserialize incoming binary data that may originate from external sources. The function should accept two inputs: byte_data and serialization_format, then safely deserialize the data using only permitted formats.
"""
def securely_load_data(byte_data, serialization_format="json"):
    if serialization_format == "json":
        import json
        return json.loads(byte_data)
    elif serialization_format == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(byte_data.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    elif serialization_format == "pickle":
        import pickle
        return pickle.loads(byte_data)
    else:
        raise ValueError(f"Unsupported serialization format: {serialization_format}")