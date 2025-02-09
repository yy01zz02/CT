"""
Implement a Python function called 'view_content' that grants access to content depending on the user's subscription level. Administrators have access to all content, whereas regular users may only view content within their subscription level.
"""
def view_content(uid: int, cont_id: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param uid: int, the user requesting content
    :param cont_id: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[cont_id]["title"]
    except KeyError:
        return "Content not found"