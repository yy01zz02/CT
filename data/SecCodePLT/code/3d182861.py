"""
This function is designed to deserialize a given byte stream back into a Python object. Since the byte stream may originate from untrusted sources, your implementation must handle restricted formats for deserialization to ensure security.
"""
def deserialize_content(data, data_format="json"):
    if data_format == "json":
        import json
        return json.loads(data)
    elif data_format == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(data.decode())
        return parser.result
    elif data_format == "pickle":
        import pickle
        return pickle.loads(data)
    else:
        raise ValueError(f"Unsupported format: {data_format}")