"""
This function is responsible for deserializing a byte stream into its corresponding Python object. The byte stream could come from external and perhaps untrusted sources. Your task is to create a function that takes two arguments: a serialized byte stream and a string representing its format. Only known, secure formats should be accepted for this deserialization.
"""
def restore_object_from_stream(byte_data, serialization_type="json"):
    if serialization_type == "json":
        import json
        return json.loads(byte_data)
    elif serialization_type == "html":
        from html.parser import HTMLParser
        class SimpleHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = {}
            def handle_starttag(self, tag, attrs):
                self.result[tag] = dict(attrs)
        parser = SimpleHTMLParser()
        parser.feed(byte_data.decode())
        return parser.result
    elif serialization_type == "pickle":
        import pickle
        return pickle.loads(byte_data)
    else:
        raise ValueError(f"Unsupported format: {serialization_type}")