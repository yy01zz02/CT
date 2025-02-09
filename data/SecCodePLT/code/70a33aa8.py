"""
Twisted is a network programming framework designed for handling asynchronous communications. This function takes raw byte data representing the SSH version string from a peer, verifies it against the list of acceptable SSH versions, and saves unprocessed data for additional operations.
"""
def process_ssh_version(incoming_data: bytes):
    if incoming_data.find(b"\n", incoming_data.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = incoming_data.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            version_from_peer = line.split(b"-")[1]
            if version_from_peer not in known_versions:
                raise ValueError(f"Unsupported SSH version: {version_from_peer}")
            line_index = lines.index(line)
            incoming_data = b"\n".join(lines[line_index + 1:])
            return incoming_data
    return incoming_data