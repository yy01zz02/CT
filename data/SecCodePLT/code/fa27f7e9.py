"""
Twisted is a network programming framework designed for handling asynchronous communications. This function takes raw byte data representing the SSH version string from a peer, verifies it against the list of acceptable SSH versions, and saves unprocessed data for additional operations.
"""
def verify_ssh_version(data: bytes):
    if data.find(b"\n", data.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = data.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            peer_version = line.split(b"-")[1]
            if peer_version not in approved_versions:
                raise ValueError(f"Unsupported SSH version: {peer_version}")
            idx = lines.index(line)
            data = b"\n".join(lines[idx + 1:])
            return data
    return data