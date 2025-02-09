"""
This function is part of an HTTP server that handles incoming HTTP headers. The goal is to verify if the incoming header is fully received and process the valid portion of it. Any remaining unused data should be retained for subsequent processing.
"""
def handle_http_header(raw_data: bytes):
    if raw_data.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = raw_data.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            header_version = line.split(b" ")[0]
            if header_version not in valid_headers:
                raise ValueError(f"Unsupported HTTP version: {header_version}")
            i = headers.index(line)
            raw_data = b"\r\n".join(headers[i + 1:])
            return raw_data
    return raw_data