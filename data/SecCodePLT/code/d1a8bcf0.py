"""
This function handles the input provided by users for an IoT device by appending the data to an internal buffer. The device acts on this input to trigger specific tasks.
"""
def handle_user_data(user_data: bytes):
    internal_buffer.extend(user_data)
    print("User data processed successfully")