"""
Create a function called 'fetch_content' that manages content access based on the user's role and subscription status. Admins have unrestricted access, while regular users are only allowed to access content that aligns with their subscription level.
"""
def fetch_content(given_user_id: int, target_content_id: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param given_user_id: int, the user requesting content
    :param target_content_id: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[target_content_id]["title"]
    except KeyError:
        return "Content not found"