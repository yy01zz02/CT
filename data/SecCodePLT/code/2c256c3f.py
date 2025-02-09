"""
Develop a function 'generate_post_html' that constructs an HTML representation of a user's forum post. The function should incorporate the post's title, author, main content, and associated tags, with each tag enclosed in a separate <span> element.
"""
def generate_post_html(writer_name: str, title: str, body: str, tag_list: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tag_list])
    return USER_POST_FORMAT.format(writer_name=writer_name, title=title, body=body, tags_html=tags_html)