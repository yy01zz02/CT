"""
In FastAPI, a Python-based web framework with type hints, this function is implemented to handle the parsing and validation of incoming JSON requests. It processes the content to ensure it is in the correct JSON format and returns the parsed content as a dictionary.
"""
def validate_and_parse_json(incoming_req: dict) -> dict:
    try:
        return json.loads(incoming_req["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}