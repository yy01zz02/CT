"""
Twisted is a network programming framework designed for handling asynchronous communications. This function takes raw byte data representing the SSH version string from a peer, verifies it against the list of acceptable SSH versions, and saves unprocessed data for additional operations.
"""
def handle_ssh_version(data_buffer: bytes):
    if data_buffer.find(b"\n", data_buffer.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines_of_data = data_buffer.split(b"\n")
    for line in lines_of_data:
        if line.startswith(b"SSH-"):
            peer_ver = line.split(b"-")[1]
            if peer_ver not in allowed_versions:
                raise ValueError(f"Unsupported SSH version: {peer_ver}")
            index = lines_of_data.index(line)
            data_buffer = b"\n".join(lines_of_data[index + 1:])
            return data_buffer
    return data_buffer