"""
This function handles the input provided by users for an IoT device by appending the data to an internal buffer. The device acts on this input to trigger specific tasks.
"""
def manage_input_data(input_data: bytes):
    input_storage.extend(input_data)
    print("Input data processed successfully")