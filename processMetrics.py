import sys
import json
import matplotlib.pyplot as plt

metrics_path = sys.argv[1]

file = open(metrics_path)
data = json.load(file)

data = data['data']['result'][0]['values']

tick_times = [float(x[1]) for x in data]

statistics_interval = 1

time_points = [x * statistics_interval for x in range(0,len(tick_times))] #should be times the interval in extract statistics
plt.plot(time_points,tick_times)


plt.xlabel("Time in S")
plt.ylabel("Average Tick time in MS")

plt.savefig('results/tick_time_plt.pdf', bbox_inches='tight')