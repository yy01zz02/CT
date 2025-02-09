"""
Manages the addition of new messages to a chat room's history in a real-time messaging system. This function is responsible for appending incoming messages to the appropriate chat room.
"""
def insert_message_in_channel(channel_name: str, participant_id: str, msg_body: str) -> bool:
    global chat_rooms
    if channel_name not in chat_rooms:
        chat_rooms[channel_name] = []
    chat_rooms[channel_name].append({"user_id": participant_id, "message": msg_body})
    return True