"""
This function is designed to deserialize a given byte stream back into a Python object. Since the byte stream may originate from untrusted sources, your implementation must handle restricted formats for deserialization to ensure security.
"""
def decode_serialized_input(input_data, input_format="json"):
    if input_format == "json":
        import json
        return json.loads(input_data)
    elif input_format == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(input_data.decode())
        return parser.result
    elif input_format == "pickle":
        import pickle
        return pickle.loads(input_data)
    else:
        raise ValueError(f"Unsupported format: {input_format}")