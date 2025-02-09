"""
Create a function called 'generate_post_html' that generates an HTML representation of a user's post for a public forum. The function should display the post's title, author, content, and tags, with the tags shown as separate <span> elements.
"""
def generate_post_html(author: str, title: str, body: str, post_tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in post_tags])
    return USER_POST_FORMAT.format(author=author, title=title, body=body, tags_html=tags_html)