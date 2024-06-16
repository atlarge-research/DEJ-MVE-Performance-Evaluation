import sys
import json
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

statistics_interval = 1
metrics_path = sys.argv[1]
metric_names_path = sys.argv[2]
results_dir_path = sys.argv[3]

with open(metric_names_path) as metric_names_file:
    metric_types = json.load(metric_names_file)
    with open(metrics_path) as file:
        data = json.load(file)
        
        for i in range(len(data)):  
            current_metric_type = metric_types[i]
            metric_data = data[i]
            metric_data = json.loads(metric_data)
            for metric in metric_data['data']['result']:
                metric_values = metric['values']
                metric_values = [float(x[1]) for x in metric_values]
                time_points = [x * statistics_interval for x in range(0,len(metric_values))]
                plt.plot(time_points,metric_values)    

            plt.xlabel("Time in Seconds")
            plt.ylabel("{0}".format(current_metric_type['y_label']))
            plt.title("{0}".format(current_metric_type['graph_title']))
            plt.autoscale()
            plt.savefig("{0}/plot{1}.png".format(results_dir_path,current_metric_type['graph_title'].replace(" ", "").replace("'","")), bbox_inches='tight')
            plt.clf()