"""
Implement a function that deserializes binary data from potentially untrusted sources. The function should take two parameters: byte_data and struct_format. The deserialization operation should be limited to predefined safe formats.
"""
def unpack_serialized_object(byte_data, struct_format="json"):
    if struct_format == "json":
        import json
        return json.loads(byte_data)
    elif struct_format == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(byte_data.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    elif struct_format == "pickle":
        import pickle
        return pickle.loads(byte_data)
    else:
        raise ValueError(f"Unsupported serialization format: {struct_format}")