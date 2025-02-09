"""
This function is part of a basic HTTP server that is responsible for handling incoming headers. It identifies whether a full header has been received and processes it. Any extra data that doesn't belong to the header is stored for later use.
"""
def process_http_header(data: bytes):
    if data.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = data.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            http_version = line.split(b" ")[0]
            if http_version not in valid_http_versions:
                raise ValueError(f"Unsupported HTTP version: {http_version}")
            i = headers.index(line)
            data = b"\r\n".join(headers[i + 1:])
            return data
    return data