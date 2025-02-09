"""
The task involves implementing a function, `purge_expired_sessions`, responsible for clearing user sessions from a database once they exceed a specific expiration time limit. The goal is to identify such sessions and remove them effectively.
"""
def purge_expired_sessions(expire_duration):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=expire_duration)
    expired_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    removed_count = 0
    
    for session in expired_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            removed_count += 1
    
    return removed_count
    return 0