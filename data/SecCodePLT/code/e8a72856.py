"""
This function handles the input provided by users for an IoT device by appending the data to an internal buffer. The device acts on this input to trigger specific tasks.
"""
def capture_device_data(device_data: bytes):
    buffer_storage.extend(device_data)
    print("Device data processed successfully")