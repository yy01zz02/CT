"""
In this task, you are required to develop a functionality that allows the removal of expired user sessions from a web application database. The function `purge_stale_sessions` will identify sessions that have surpassed a given expiration threshold and then proceed to delete them accordingly.
"""
def purge_stale_sessions(expiry_time):
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=expiry_time)
    stale_sessions = db.query("SELECT id FROM sessions WHERE last_activity < ?", (expiration_threshold,))
    deleted_count = 0
    
    for session in stale_sessions:
        if db.execute("DELETE FROM sessions WHERE id = ?", (session['id'],)):
            deleted_count += 1
    
    return deleted_count
    return 0