"""
Integrates new messages into a chat room's conversation log within a real-time messaging platform. This function is tasked with incorporating incoming messages into the designated chat room's history.
"""
def insert_chat_message(chat_room_id: str, author_id: str, message_content: str) -> bool:
    global chat_rooms
    if chat_room_id not in chat_rooms:
        chat_rooms[chat_room_id] = []
    chat_rooms[chat_room_id].append({"user_id": author_id, "message": message_content})
    return True