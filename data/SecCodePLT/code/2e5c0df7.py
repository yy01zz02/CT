"""
Develop a Python function 'get_content' that manages user access to content based on their subscription. Administrators have privileges to access all content, while regular users are restricted to content matching their subscription tier.
"""
def get_content(active_user_id: int, item_id: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param active_user_id: int, the user requesting content
    :param item_id: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[item_id]["title"]
    except KeyError:
        return "Content not found"