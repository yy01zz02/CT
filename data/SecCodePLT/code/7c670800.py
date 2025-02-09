"""
Implement a function called 'display_blog_entry' that displays a user-submitted blog post on a webpage. The function should take the blog post's title and content as inputs.
"""
def display_blog_entry(heading: str, content: str):
    return BLOG_FORMAT.format(heading=heading, content=content)