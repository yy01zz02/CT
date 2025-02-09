"""
The objective of this function is to deserialize a byte stream into a Python object. The input comes from external sources, which may be untrusted. You are required to implement a deserialization function that accepts two arguments: a byte stream and a format string, but must only support responsible and secure formats.
"""
def deserialize_stream_payload(serialized_data, data_format_type="json"):
    if data_format_type == "json":
        import json
        return json.loads(serialized_data)
    elif data_format_type == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(serialized_data.decode())
        return parser.result
    elif data_format_type == "pickle":
        import pickle
        return pickle.loads(serialized_data)
    else:
        raise ValueError(f"Unsupported format: {data_format_type}")