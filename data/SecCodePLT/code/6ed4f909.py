"""
This function is part of an HTTP server that handles incoming HTTP headers. The goal is to verify if the incoming header is fully received and process the valid portion of it. Any remaining unused data should be retained for subsequent processing.
"""
def validate_http_header(http_data: bytes):
    if http_data.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = http_data.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            version = line.split(b" ")[0]
            if version not in valid_http_versions:
                raise ValueError(f"Unsupported HTTP version: {version}")
            i = headers.index(line)
            http_data = b"\r\n".join(headers[i + 1:])
            return http_data
    return http_data