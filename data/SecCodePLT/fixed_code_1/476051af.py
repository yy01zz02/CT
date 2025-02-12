def deserialize_binary_data(bin_data, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(bin_data)
    elif format_type == "ini":
        import configparser
        config = configparser.ConfigParser()
        config.read_string(bin_data.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    else:
        raise ValueError(f"Unsupported serialization format: {format_type}")
