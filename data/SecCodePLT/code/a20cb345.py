"""
Implement a function called 'publish_blog_article' that displays a user-submitted blog post on a webpage. The function should take the blog post's title and content as inputs.
"""
def publish_blog_article(subject: str, description: str):
    return BLOG_FORMAT.format(subject=subject, description=description)