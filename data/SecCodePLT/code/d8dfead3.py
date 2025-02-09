"""
The task involves implementing a function, `delete_expired_sessions`, responsible for clearing user sessions from a database once they exceed a specific expiration time limit. The goal is to identify such sessions and remove them effectively.
"""
def delete_expired_sessions(session_expiration):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=session_expiration)
    expired_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    deleted_count = 0
    
    for session in expired_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            deleted_count += 1
    
    return deleted_count
    return 0