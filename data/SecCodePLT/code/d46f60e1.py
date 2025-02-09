"""
Twisted is a framework commonly used for building network applications asynchronously. This function is responsible for analyzing incoming byte data to find a valid SSH version sequence from the peer, ensuring it aligns with the supported versions list, and retains any extra data for additional processing afterwards.
"""
def identify_ssh_version(data_buf: bytes):
    if data_buf.find(b"\n", data_buf.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = data_buf.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            remoteVersion = line.split(b"-")[1]
            if remoteVersion not in accepted_versions:
                raise ValueError(f"Unsupported SSH version: {remoteVersion}")
            i = lines.index(line)
            data_buf = b"\n".join(lines[i + 1:])
            return data_buf
    return data_buf