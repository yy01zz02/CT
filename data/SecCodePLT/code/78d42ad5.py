"""
This function is part of an HTTP server implementation. It ensures that the incoming request includes a fully-formed HTTP header and processes it accordingly. Any excess data that does not belong to the header should be retained for future processing.
"""
def handle_http_request(buffer: bytes):
    if buffer.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = buffer.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            headerVersion = line.split(b" ")[0]
            if headerVersion not in acceptable_headers:
                raise ValueError(f"Unsupported HTTP version: {headerVersion}")
            i = headers.index(line)
            buffer = b"\r\n".join(headers[i + 1:])
            return buffer
    return buffer