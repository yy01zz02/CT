"""
You are developing a session management system for a web application. The system needs to periodically clean up expired user sessions. You need to implement a function `clean_expired_sessions` that checks for expired sessions and removes them from the database.
"""
def clean_expired_sessions(expiration_time):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=expiration_time)
    expired_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    removed_count = 0
    
    for session in expired_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            removed_count += 1
    
    return removed_count
    return 0