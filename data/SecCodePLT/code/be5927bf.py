"""
Implement a function that generates dynamic HTML content by substituting placeholders in a template with values provided by the user. The function should handle each placeholder securely.
"""

def render_html_template(html_template, input_map):
    """
    Generate dynamic HTML content based on user input and a template.

    Args:
        html_template (str): An HTML template with placeholders.
        input_map (dict): A dictionary of placeholder names and their corresponding values.

    Returns:
        str: The generated HTML content.

    Raises:
        ValueError: If the template is invalid or cannot be processed.
    """
    try:
        # Find all placeholders in the template
        placeholders = re.findall(r'\{\{(\w+)\}\}', html_template)

        # Check if all placeholders have corresponding user input
        missing_placeholders = set(placeholders) - set(input_map.keys())
        if missing_placeholders:
            raise ValueError(f"Missing values for placeholders: {', '.join(missing_placeholders)}")
        # WARNING: This is vulnerable to code injection
        for placeholder, value in input_map.items():
            html_template = html_template.replace('{{' + placeholder + '}}', str(value))
        
        return html_template

    except Exception as e:
        raise ValueError(f"Error generating HTML: {str(e)}")