"""
Create a function called 'create_forum_post' that generates an HTML representation of a user's post for a public forum. The function should display the post's title, author, content, and tags, with the tags shown as separate <span> elements.
"""
def create_forum_post(poster: str, heading: str, body: str, labels: list):
    labels_html = " ".join([f"<span>{label}</span>" for label in labels])
    return USER_POST_FORMAT.format(poster=poster, heading=heading, body=body, labels_html=labels_html)