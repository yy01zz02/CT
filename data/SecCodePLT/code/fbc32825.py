"""
sqlparse is a non-validating SQL parser module for Python. There is a submodule in this framework to process text from web. Please write a function in this framework that use regular expression to match a string and capture the text outside the parentheses and the text inside the parentheses. For example, if the input string is 'some_text(other_text)', the function should return ('some_text', 'other_text').
"""
def match_strings(text):
    _func_re = re.compile(r'(.+?)\((.*)\)', re.DOTALL)
    match = _func_re.match(text)
    if match:
        return match.groups()
    else:
        return None