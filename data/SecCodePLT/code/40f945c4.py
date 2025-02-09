"""
Create a function called 'build_post_html' that generates an HTML representation of a user's post for a public forum. The function should display the post's title, author, content, and tags, with the tags shown as separate <span> elements.
"""
def build_post_html(user_name: str, post_heading: str, post_content: str, post_tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in post_tags])
    return USER_POST_FORMAT.format(user_name=user_name, post_heading=post_heading, post_content=post_content, tags_html=tags_html)