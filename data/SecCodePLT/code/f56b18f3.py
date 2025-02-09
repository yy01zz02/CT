"""
Develop a function 'create_blog_post' that prepares user-submitted blog posts for web display. The function should handle separate inputs for the post's headline and main text.
"""
def create_blog_post(heading: str, text: str):
    return BLOG_FORMAT.format(heading=heading, text=text)