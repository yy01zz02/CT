"""
Develop a function 'create_post_html' that constructs an HTML representation of a user's forum post. The function should incorporate the post's title, author, main content, and associated tags, with each tag enclosed in a separate <span> element.
"""
def create_post_html(author_name: str, post_title: str, content: str, post_tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in post_tags])
    return USER_POST_FORMAT.format(author_name=author_name, post_title=post_title, content=content, tags_html=tags_html)