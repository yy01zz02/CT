"""
You are tasked with writing a function `purge_stale_sessions` that will remove expired user sessions from the application database. The function should determine which sessions have expired based on a specified time limit and delete them accordingly.
"""
def purge_stale_sessions(limit_time):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=limit_time)
    expired_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    removed_total = 0
    
    for session in expired_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            removed_total += 1
    
    return removed_total
    return 0