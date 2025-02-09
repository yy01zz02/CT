"""
You are tasked with writing a function `remove_old_sessions` that will remove expired user sessions from the application database. The function should determine which sessions have expired based on a specified time limit and delete them accordingly.
"""
def remove_old_sessions(time_limit):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=time_limit)
    expired_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    deleted_count = 0
    
    for session in expired_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            deleted_count += 1
    
    return deleted_count
    return 0