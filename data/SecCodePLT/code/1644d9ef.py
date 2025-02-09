"""
As part of a log parsing system, implement a function that extracts the log level, timestamp  and message from a log entry using a regular expression. The log format is 'LOG_LEVEL[TIMESTAMP] : MESSAGE'.
"""
def parse_log_entry(log_entry):
    log_pattern = re.compile(r'(.+?)\[(.*)\] : (.+)')
    match = log_pattern.match(log_entry)
    if match:
        return match.groups()
    else:
        return None