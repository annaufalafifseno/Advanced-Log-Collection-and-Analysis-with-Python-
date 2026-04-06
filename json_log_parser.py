import json

with open('json_logs.json', 'r') as log_file:
    logs = json.load(log_file)

for log in logs:
    print(f"Timestamp: {log['timestamp']}")
    print(f"Level: {log['level']}")
    print(f"Message: {log['message']}")
    print("-" * 50)