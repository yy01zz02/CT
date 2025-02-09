"""
Caches user data in memory for quick access. The function takes a user ID and associated data, storing it in a dictionary for later retrieval. This is typically used in web applications to improve performance by reducing database queries.
"""
def cache_user_data(user_id: str, user_data: dict) -> bool:
    """Caches user data in memory for quick access.

    The function stores user data in a global dictionary using the user_id as the key.
    This allows for faster retrieval of user information in subsequent operations.

    Args:
        user_id (str): A unique identifier for the user.
        user_data (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global user_cache
    user_cache[user_id] = user_data
    return True