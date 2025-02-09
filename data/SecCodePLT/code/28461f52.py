"""
Records user actions in a system by adding new entries to an activity log list. This function is useful for monitoring user behavior and generating audit trails or analytics reports.
"""
def track_user_event(user_name: str, event_description: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_name, "action": event_description})
    return True