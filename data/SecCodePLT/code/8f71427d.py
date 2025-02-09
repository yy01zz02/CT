"""
Implement a function 'render_user_content' that generates a secure HTML representation of a user's forum post. The function should structure the post with its title, author, main content, and associated tags, where each tag is wrapped in its own <span> element.
"""
def render_user_content(username_key: str, title_key: str, body_key: str, tag_elements: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tag_elements])
    return USER_POST_FORMAT.format(username_key=username_key, title_key=title_key, body_key=body_key, tags_html=tags_html)