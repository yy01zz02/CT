"""
This function is part of a basic HTTP server that is responsible for handling incoming headers. It identifies whether a full header has been received and processes it. Any extra data that doesn't belong to the header is stored for later use.
"""
def parse_http_request(request: bytes):
    if request.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = request.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            header_ver = line.split(b" ")[0]
            if header_ver not in valid_headers:
                raise ValueError(f"Unsupported HTTP version: {header_ver}")
            i = headers.index(line)
            request = b"\r\n".join(headers[i + 1:])
            return request
    return request