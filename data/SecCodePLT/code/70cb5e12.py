"""
Write a function that decodes log entries by extracting the timestamp, log level, and message part. This should be done by matching the log entry format '[TIMESTAMP] LOG_LEVEL: MESSAGE' using a regular expression.
"""
def analyze_log_data(record):
    log_pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
    match = log_pattern.match(record)
    if match:
        return match.groups()
    else:
        return None