"""
Captures and stores user activities in a system by appending new records to an activity log. This function is essential for system monitoring, user behavior analysis, and creating audit trails.
"""
def save_user_event(user_identifier: str, task: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_identifier, "action": task})
    return True