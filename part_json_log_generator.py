import json
import datetime

logs = [
    {
        "timestamp": str(datetime.datetime.now()),
        "level": "INFO",
        "message": "User login successful"
    },
    {
        "timestamp": str(datetime.datetime.now()),
        "level": "WARNING",
        "message": "Failed login attempt"
    },
    {
        "timestamp": str(datetime.datetime.now()),
        "level": "ERROR",
        "message": "Database connection timeout"
    }
]

with open('json_logs.json', 'w') as log_file:
    json.dump(logs, log_file, indent=4)