"""
Implement a function to decode log entries by extracting the timestamp, log level, and accompanying message. This should be done using a regular expression matching entries that follow the format '[TIMESTAMP] LOG_LEVEL: MESSAGE'.
"""
def extract_log_data(log_line):
    log_pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
    match = log_pattern.match(log_line)
    if match:
        return match.groups()
    else:
        return None