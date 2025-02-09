"""
Develop a function 'format_blog_entry' that prepares user-submitted blog posts for web display. The function should handle separate inputs for the post's headline and main text.
"""
def format_blog_entry(headline: str, content: str):
    return BLOG_FORMAT.format(headline=headline, content=content)