"""
Develop a function to extract key components from a log entry, including the log level, timestamp and message. This should be achieved by employing a regular expression to match the log format 'LOG_LEVEL[TIMESTAMP] : MESSAGE'.
"""
def extract_log_data(log_text):
    log_pattern = re.compile(r'(.+?)\[(.*)\] : (.+)')
    match = log_pattern.match(log_text)
    if match:
        return match.groups()
    else:
        return None