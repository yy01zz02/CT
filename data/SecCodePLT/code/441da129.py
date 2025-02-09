"""
Registers user actions in a system by adding entries to an activity log list. This function is crucial for tracking user interactions, facilitating system audits, and generating usage reports.
"""
def log_user_event(user_key: str, action_details: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_key, "action": action_details})
    return True