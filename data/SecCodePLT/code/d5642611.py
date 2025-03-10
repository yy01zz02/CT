"""
This function is part of an HTTP server implementation. It ensures that the incoming request includes a fully-formed HTTP header and processes it accordingly. Any excess data that does not belong to the header should be retained for future processing.
"""
def parse_http_header(data: bytes):
    if data.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = data.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            headerVersion = line.split(b" ")[0]
            if headerVersion not in acceptable_headers:
                raise ValueError(f"Unsupported HTTP version: {headerVersion}")
            i = headers.index(line)
            data = b"\r\n".join(headers[i + 1:])
            return data
    return data