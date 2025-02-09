"""
Records user actions in a system by adding new entries to an activity log list. This function is useful for monitoring user behavior and generating audit trails or analytics reports.
"""
def record_user_action(uid: str, act_description: str) -> bool:
    global activity_log
    activity_log.append({"user_id": uid, "action": act_description})
    return True