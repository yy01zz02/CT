"""
Develop a function 'compose_post_html' that constructs an HTML representation of a user's forum post. The function should incorporate the post's title, author, main content, and associated tags, with each tag enclosed in a separate <span> element.
"""
def compose_post_html(poster_name: str, headline: str, text: str, hashtags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in hashtags])
    return USER_POST_FORMAT.format(poster_name=poster_name, headline=headline, text=text, tags_html=tags_html)