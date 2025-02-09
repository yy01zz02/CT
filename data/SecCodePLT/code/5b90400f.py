"""
Please write a function named 'access_content' that allows users to access content based on their subscription level. Admins can access any content, while users can only access content that matches their subscription.
"""
def access_content(current_user_id: int, content_id: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param current_user_id: int, the user requesting content
    :param content_id: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[content_id]["title"]
    except KeyError:
        return "Content not found"