"""
Captures and stores user activities in a system by appending new records to an activity log. This function is essential for system monitoring, user behavior analysis, and creating audit trails.
"""
def track_user_operation(account: str, operation: str) -> bool:
    global activity_log
    activity_log.append({"user_id": account, "action": operation})
    return True