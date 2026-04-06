import re

with open('generated_logs.log', 'r') as log_file:
    logs = log_file.readlines()

log_pattern = re.compile(
    r'(?P<timestamp>[\d-]+\s[\d:]+),\d+\s-\s(?P<logger_name>\w+)\s-\s(?P<level>\w+)\s-\s(?P<message>.+)'
)

for log in logs:
    match = log_pattern.match(log)
    if match:
        log_details = match.groupdict()
        print(f"Timestamp: {log_details['timestamp']}")
        print(f"Level: {log_details['level']}")
        print(f"Message: {log_details['message']}")
        print("-" * 50)