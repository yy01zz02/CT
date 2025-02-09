"""
Logs user activity by appending new entries to a list. The function is designed to keep track of user actions in a system, which can be used for auditing or analytics purposes.
"""
def log_user_activity(user_id: str, action: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_id, "action": action})
    return True