import pandas as pd

# Load log
log_data = pd.read_csv(
    'generated_logs.log',
    sep=' - ',
    names=['timestamp', 'logger', 'level', 'message'],
    engine='python'
)

# Ringkasan level log
log_summary = log_data['level'].value_counts()

print("Log Level Summary:")
print(log_summary)

# Filter ERROR
error_logs = log_data[log_data['level'] == 'ERROR']

print("\nError Logs:")
print(error_logs)

import matplotlib.pyplot as plt

log_summary.plot(kind='bar')

plt.title('Log Level Distribution')
plt.xlabel('Log Levels')
plt.ylabel('Frequency')

plt.show()