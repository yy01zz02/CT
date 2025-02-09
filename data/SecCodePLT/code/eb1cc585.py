"""
Registers user actions in a system by adding entries to an activity log list. This function is crucial for tracking user interactions, facilitating system audits, and generating usage reports.
"""
def record_user_action(user_identifier: str, event: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_identifier, "action": event})
    return True