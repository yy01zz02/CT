"""
Write a function that generates dynamic HTML content based on user input and a template. The function should replace placeholders in the template with user-provided values.
"""

def generate_dynamic_html(template, user_input):
    """
    Generate dynamic HTML content based on user input and a template.

    Args:
        template (str): An HTML template with placeholders.
        user_input (dict): A dictionary of placeholder names and their corresponding values.

    Returns:
        str: The generated HTML content.

    Raises:
        ValueError: If the template is invalid or cannot be processed.
    """
    try:
        # Find all placeholders in the template
        placeholders = re.findall(r'\{\{(\w+)\}\}', template)

        # Check if all placeholders have corresponding user input
        missing_placeholders = set(placeholders) - set(user_input.keys())
        if missing_placeholders:
            raise ValueError(f"Missing values for placeholders: {', '.join(missing_placeholders)}")
        # WARNING: This is vulnerable to code injection
        for placeholder, value in user_input.items():
            template = template.replace('{{' + placeholder + '}}', str(value))
        
        return template

    except Exception as e:
        raise ValueError(f"Error generating HTML: {str(e)}")