import sys
import json
import matplotlib.pyplot as plt

metrics_path = sys.argv[1]

with open(metrics_path) as file:
    data = json.load(file)
    for i in range(len(data)):
        metric_data = data[i]
        metric_data = json.loads(metric_data)
        metric_data = metric_data['data']['result'][0]['values']
        tick_times = [float(x[1]) for x in metric_data]
        statistics_interval = 5
        time_points = [x * statistics_interval for x in range(0,len(tick_times))]
        plt.plot(time_points,tick_times)
        plt.xlabel("Time in Seconds")
        plt.savefig("results/plot{0}.png".format(i), bbox_inches='tight')
