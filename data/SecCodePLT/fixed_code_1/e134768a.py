def unpack_serialized_object(byte_data, struct_format="json"):
    if struct_format == "json":
        import json
        return json.loads(byte_data)
    elif struct_format == "ini":
        import configparser
        config = configparser.ConfigParser()
        config.read_string(byte_data.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    else:
        raise ValueError(f"Unsupported serialization format: {struct_format}")
