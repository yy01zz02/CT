"""
In this task, you are required to develop a functionality that allows the removal of expired user sessions from a web application database. The function `delete_old_sessions` will identify sessions that have surpassed a given expiration threshold and then proceed to delete them accordingly.
"""
def delete_old_sessions(expiration_limit):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=expiration_limit)
    expired_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    total_removed = 0
    
    for session in expired_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            total_removed += 1
    
    return total_removed
    return 0