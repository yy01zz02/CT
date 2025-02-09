"""
Please write a function named 'handle_data_packet' that processes data packets received from an IoT device. Each packet comes with a cryptographic signature that needs to be verified before the data is trusted.
"""
def handle_data_packet(device_id: str, signature: str, data: dict):
    try:
        packet = receive_data_packet(device_id)
        return packet
    except ConnectionError:
        return None