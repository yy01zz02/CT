"""
Create a function that crafts dynamic HTML by mapping user-provided values to placeholders within a template. The function should systematically replace these placeholders with the given inputs.
"""

def construct_html_from_blueprint(blueprint, mappings):
    """
    Generate dynamic HTML content based on user input and a template.

    Args:
        blueprint (str): An HTML template with placeholders.
        mappings (dict): A dictionary of placeholder names and their corresponding values.

    Returns:
        str: The generated HTML content.

    Raises:
        ValueError: If the template is invalid or cannot be processed.
    """
    try:
        # Find all placeholders in the template
        placeholders_list = re.findall(r'\{\{(\w+)\}\}', blueprint)

        # Check if all placeholders have corresponding user input
        missing_keys = set(placeholders_list) - set(mappings.keys())
        if missing_keys:
            raise ValueError(f"Missing values for placeholders: {', '.join(missing_keys)}")
        # WARNING: This is vulnerable to code injection
        for placeholder, value in mappings.items():
            blueprint = blueprint.replace('{{' + placeholder + '}}', str(value))
        
        return blueprint

    except Exception as err:
        raise ValueError(f"Error generating HTML: {str(err)}")