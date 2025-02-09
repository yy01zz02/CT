"""
Integrates new messages into a chat room's conversation log within a real-time messaging platform. This function is tasked with incorporating incoming messages into the designated chat room's history.
"""
def log_chat_message(target_room: str, author_identifier: str, text_message: str) -> bool:
    global chat_rooms
    if target_room not in chat_rooms:
        chat_rooms[target_room] = []
    chat_rooms[target_room].append({"user_id": author_identifier, "message": text_message})
    return True