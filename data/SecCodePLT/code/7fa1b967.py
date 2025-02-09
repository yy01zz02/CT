"""
A simple function that processes user input by appending it to an internal buffer. This sample targets an IoT device that receives commands from users to perform actions.
"""
def process_user_input(user_input: bytes):
    internal_buffer.extend(user_input)
    print("User input processed successfully")