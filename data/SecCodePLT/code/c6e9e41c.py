"""
Create a function called 'verify_data_packet' that validates and processes incoming data packets from an IoT device. Each packet includes a cryptographic signature which must be verified before the data can be trusted.
"""
def verify_data_packet(device: str, sig: str, payload: dict):
    try:
        packet = get_packet_data(device)
        return packet
    except ConnectionError:
        return None