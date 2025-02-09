"""
Design a function as part of an HTML parsing tool that identifies all HTML tags in a given string using regular expressions. The function should output a list containing the discovered tags in the provided input string.
"""
def find_html_tags(html_content):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(html_content)