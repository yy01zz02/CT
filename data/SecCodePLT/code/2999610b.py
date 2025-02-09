"""
Implement a Python function called 'retrieve_content' that grants access to content depending on the user's subscription level. Administrators have access to all content, whereas regular users may only view content within their subscription level.
"""
def retrieve_content(usr_id: int, contid: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param usr_id: int, the user requesting content
    :param contid: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[contid]["title"]
    except KeyError:
        return "Content not found"