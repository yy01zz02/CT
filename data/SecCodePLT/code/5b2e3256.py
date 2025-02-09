"""
Implement a Python function called 'fetch_content' that grants access to content depending on the user's subscription level. Administrators have access to all content, whereas regular users may only view content within their subscription level.
"""
def fetch_content(user_id: int, cid: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param user_id: int, the user requesting content
    :param cid: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[cid]["title"]
    except KeyError:
        return "Content not found"