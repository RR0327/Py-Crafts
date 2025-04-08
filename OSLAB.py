import numpy as np
import pandas as pd

# Define Processes
tasks = [
    {"Process": "P1", "Arrival Time": 0, "Burst Time": 10},
    {"Process": "P2", "Arrival Time": 2, "Burst Time": 4},
    {"Process": "P3", "Arrival Time": 4, "Burst Time": 2},
    {"Process": "P4", "Arrival Time": 6, "Burst Time": 8}
]

df = pd.DataFrame(tasks)
df = df.sort_values(by=["Arrival Time", "Burst Time"]).reset_index(drop=True)

waiting_time = []
turnaround_time = []
completion_time = 0

for i, row in df.iterrows():
    if completion_time < row['Arrival Time']:
        completion_time = row['Arrival Time']
    waiting_time.append(completion_time - row['Arrival Time'])
    completion_time += row['Burst Time']
    turnaround_time.append(completion_time - row['Arrival Time'])

df['Waiting Time'] = waiting_time
df['Turnaround Time'] = turnaround_time

# Compute Average Metrics
avg_wt = np.mean(waiting_time)
avg_tat = np.mean(turnaround_time)

print(df)
print(f"\nAverage Waiting Time: {avg_wt:.2f} ms")
print(f"Average Turnaround Time: {avg_tat:.2f} ms")