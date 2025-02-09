"""
Create a function called 'process_data_packet' that validates and processes incoming data packets from an IoT device. Each packet includes a cryptographic signature which must be verified before the data can be trusted.
"""
def process_data_packet(dev_id: str, sign: str, payload: dict):
    try:
        packet = get_data_packet(dev_id)
        return packet
    except ConnectionError:
        return None