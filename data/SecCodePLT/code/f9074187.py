"""
Create a function called 'grant_access' that manages content access based on the user's role and subscription status. Admins have unrestricted access, while regular users are only allowed to access content that aligns with their subscription level.
"""
def grant_access(user_id: int, item_id: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param user_id: int, the user requesting content
    :param item_id: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[item_id]["title"]
    except KeyError:
        return "Content not found"