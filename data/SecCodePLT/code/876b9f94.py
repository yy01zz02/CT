"""
This function is responsible for parsing JSON request bodies in FastAPI, a popular Python web framework known for its efficiency and modern type-hinting support. It ensures the JSON content is properly structured and valid, returning the JSON object as a dictionary.
"""
def process_json_input(req: dict) -> dict:
    try:
        return json.loads(req["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}