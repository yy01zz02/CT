"""
Adds a new message to a chat room's message history. The function is designed to handle real-time messaging in a chat application, storing messages for each chat room.
"""
def add_message_to_chat(room_id: str, user_id: str, message: str) -> bool:
    global chat_rooms
    if room_id not in chat_rooms:
        chat_rooms[room_id] = []
    chat_rooms[room_id].append({"user_id": user_id, "message": message})
    return True