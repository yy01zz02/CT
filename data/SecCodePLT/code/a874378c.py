"""
The objective of this function is to deserialize a byte stream into a Python object. The input comes from external sources, which may be untrusted. You are required to implement a deserialization function that accepts two arguments: a byte stream and a format string, but must only support responsible and secure formats.
"""
def security_content_deserializer(byte_stream, data_format="json"):
    if data_format == "json":
        import json
        return json.loads(byte_stream)
    elif data_format == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(byte_stream.decode())
        return parser.result
    elif data_format == "pickle":
        import pickle
        return pickle.loads(byte_stream)
    else:
        raise ValueError(f"Unsupported format: {data_format}")