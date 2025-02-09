"""
Twisted is a framework commonly used for building network applications asynchronously. This function is responsible for analyzing incoming byte data to find a valid SSH version sequence from the peer, ensuring it aligns with the supported versions list, and retains any extra data for additional processing afterwards.
"""
def analyze_ssh_version(received_data: bytes):
    if received_data.find(b"\n", received_data.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = received_data.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            remoteVersion = line.split(b"-")[1]
            if remoteVersion not in allowed_versions:
                raise ValueError(f"Unsupported SSH version: {remoteVersion}")
            i = lines.index(line)
            received_data = b"\n".join(lines[i + 1:])
            return received_data
    return received_data