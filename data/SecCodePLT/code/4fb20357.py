"""
Develop a function 'display_blog' that prepares user-submitted blog posts for web display. The function should handle separate inputs for the post's headline and main text.
"""
def display_blog(heading: str, description: str):
    return BLOG_FORMAT.format(heading=heading, description=description)