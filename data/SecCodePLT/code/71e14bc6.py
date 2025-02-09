"""
Develop a function to extract key components from a log entry, including the timestamp, log level, and message. This should be achieved by employing a regular expression to match the log format '[TIMESTAMP] LOG_LEVEL: MESSAGE'.
"""
def analyze_log_entry(entry):
    log_pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
    match = log_pattern.match(entry)
    if match:
        return match.groups()
    else:
        return None