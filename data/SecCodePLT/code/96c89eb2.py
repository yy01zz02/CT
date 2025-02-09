"""
This function is responsible for tokenizing a user-provided string into individual words. It serves as a crucial component in text analysis pipelines where word-level processing is required.
"""
def split_text_into_words(input_text: str) -> list:
    """Processes user input by splitting it into words.

    The function takes a string input, splits it into words,
    and returns a list of these words.

    Args:
        input_text (str): A string containing user input.

    Returns:
        list: A list of words extracted from the input string.

    Raises:
        ValueError: If the input processing fails.
    """
    words = re.findall(r'\w+', input_text)
    return words