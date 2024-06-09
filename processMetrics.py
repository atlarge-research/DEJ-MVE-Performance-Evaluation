import sys
import json
import matplotlib.pyplot as plt

metrics_path = sys.argv[1]

with open(metrics_path) as file:
    data = json.load(file)
    for i in range(len(data)):
        data = data[i]
        data = json.loads(data)
        data = data['data']['result'][0]['values']
        tick_times = [float(x[1]) for x in data]
        statistics_interval = 5
        time_points = [x * statistics_interval for x in range(0,len(tick_times))] #should be times the interval in extract statistics
        plt.plot(time_points,tick_times)
        plt.xlabel("Time in Seconds")
        plt.savefig("results/plot{0}.pdf".format(i), bbox_inches='tight')
