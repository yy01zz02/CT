"""
Records user actions in a system by adding new entries to an activity log list. This function is useful for monitoring user behavior and generating audit trails or analytics reports.
"""
def save_user_interaction(user_alias: str, interaction_desc: str) -> bool:
    global activity_log
    activity_log.append({"user_id": user_alias, "action": interaction_desc})
    return True