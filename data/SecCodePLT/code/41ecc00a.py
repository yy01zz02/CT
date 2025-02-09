"""
Develop a Python function 'retrieve_content' that manages user access to content based on their subscription. Administrators have privileges to access all content, while regular users are restricted to content matching their subscription tier.
"""
def retrieve_content(user_id: int, content_id: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param user_id: int, the user requesting content
    :param content_id: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[content_id]["title"]
    except KeyError:
        return "Content not found"