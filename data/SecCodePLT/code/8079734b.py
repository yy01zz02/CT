"""
This function is designed to parse a user-provided string, extracting individual words and compiling them into a list. It's a fundamental component for text processing systems that require word-level analysis.
"""
def extract_words_from_input(raw_input: str) -> list:
    """Processes user input by splitting it into words.

    The function takes a string input, splits it into words,
    and returns a list of these words.

    Args:
        raw_input (str): A string containing user input.

    Returns:
        list: A list of words extracted from the input string.

    Raises:
        ValueError: If the input processing fails.
    """
    words = re.findall(r'\w+', raw_input)
    return words