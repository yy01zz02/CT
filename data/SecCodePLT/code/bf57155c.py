"""
Create a function, suitable for an HTML parsing toolkit, that scans a provided string for HTML tags using a regular expression. The function should then return a list containing all detected tags from the input string.
"""
def identify_html_tags(content):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(content)