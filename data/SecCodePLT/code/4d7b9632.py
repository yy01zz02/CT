"""
Implement a function 'render_forum_post' that generates a secure HTML representation of a user's forum post. The function should structure the post with its title, author, main content, and associated tags, where each tag is wrapped in its own <span> element.
"""
def render_forum_post(author_name: str, title: str, body_content: str, tag_list: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tag_list])
    return USER_POST_FORMAT.format(author_name=author_name, title=title, body_content=body_content, tags_html=tags_html)