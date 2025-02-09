"""
Implements a message addition feature for a chat application. This function appends new messages to a specific chat room's history, facilitating real-time communication.
"""
def insert_message_in_chat(chat_id: str, sender_id: str, msg: str) -> bool:
    global chat_rooms
    if chat_id not in chat_rooms:
        chat_rooms[chat_id] = []
    chat_rooms[chat_id].append({"user_id": sender_id, "message": msg})
    return True