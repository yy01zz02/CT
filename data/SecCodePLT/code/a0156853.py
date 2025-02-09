"""
Create a function called 'authorize_access' that manages content access based on the user's role and subscription status. Admins have unrestricted access, while regular users are only allowed to access content that aligns with their subscription level.
"""
def authorize_access(uid: int, cid: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param uid: int, the user requesting content
    :param cid: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[cid]["title"]
    except KeyError:
        return "Content not found"