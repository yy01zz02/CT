"""
Please write a function named 'render_user_post' that displays a user-generated post in a public forum. The tags should be displayed as <span> elements separated by spaces.
"""
def render_user_post(username: str, post_title: str, post_body: str, tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tags])
    return USER_POST_FORMAT.format(username=username, post_title=post_title, post_body=post_body, tags_html=tags_html)