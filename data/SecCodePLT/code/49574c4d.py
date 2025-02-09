"""
Design a function as part of an HTML parsing tool that identifies all HTML tags in a given string using regular expressions. The function should output a list containing the discovered tags in the provided input string.
"""
def extract_html_elements(document):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(document)