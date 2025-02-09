"""
Create a function 'render_article_page' that formats and displays user-submitted blog posts on a webpage. The function should accept two separate inputs for the blog post's title and main content.
"""
def render_article_page(headline: str, content: str):
    return BLOG_FORMAT.format(headline=headline, content=content)