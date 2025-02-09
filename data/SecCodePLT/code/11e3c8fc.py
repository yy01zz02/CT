"""
Implement a function 'render_blog_post' that generates a secure HTML representation of a user's forum post. The function should structure the post with its title, author, main content, and associated tags, where each tag is wrapped in its own <span> element.
"""
def render_blog_post(author_id: str, post_heading: str, content: str, labels: list):
    label_html = " ".join([f"<span>{label}</span>" for label in labels])
    return USER_POST_FORMAT.format(author_id=author_id, post_heading=post_heading, content=content, label_html=label_html)