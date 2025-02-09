"""
This function is responsible for deserializing a byte stream into its corresponding Python object. The byte stream could come from external and perhaps untrusted sources. Your task is to create a function that takes two arguments: a serialized byte stream and a string representing its format. Only known, secure formats should be accepted for this deserialization.
"""
def decode_data_stream(data, data_format="json"):
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