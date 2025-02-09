"""
Implement a function called 'process_packet_data' which is responsible for authenticating and processing data packets originating from IoT devices. Each packet contains a cryptographic signature that needs to be validated before the data can be trusted.
"""
def process_packet_data(id_device: str, packet_signature: str, packet_data: dict):
    try:
        packet = receive_data_packet(id_device)
        return packet
    except ConnectionError:
        return None