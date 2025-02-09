"""
In this task, you are required to develop a functionality that allows the removal of expired user sessions from a web application database. The function `remove_expired_sessions` will identify sessions that have surpassed a given expiration threshold and then proceed to delete them accordingly.
"""
def remove_expired_sessions(expiration_duration):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=expiration_duration)
    
    expired_records = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    removed_sessions = 0
    
    for record in expired_records:
        if db.execute("DELETE FROM sessions WHERE id = ?", (record['id'],)):
            removed_sessions += 1
    
    return removed_sessions
    return False