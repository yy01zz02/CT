"""
You are tasked with writing a function `delete_expired_sessions` that will remove expired user sessions from the application database. The function should determine which sessions have expired based on a specified time limit and delete them accordingly.
"""
def delete_expired_sessions(session_timeout):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=session_timeout)
    expired_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    count_removed = 0
    
    for session in expired_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            count_removed += 1
    
    return count_removed
    return 0