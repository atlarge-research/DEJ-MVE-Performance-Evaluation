import sys
import json
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import numpy as np

statistics_interval = 1
metrics_path = sys.argv[1]
metric_names_path = sys.argv[2]
results_dir_path = sys.argv[3]

curr_time = (datetime.datetime.now().strftime("%m/%d-%H:%M:%S")).replace(" ","")


with open(metric_names_path) as metric_names_file:
    metric_types = json.load(metric_names_file)
    with open(metrics_path) as file:
        data = json.load(file)
        
        for i in range(len(data)):  
            current_metric_type = metric_types[i]
            metric_data = data[i]
            metric_data = json.loads(metric_data)
            all_values = []
            for metric in metric_data['data']['result']:
                metric_values = metric['values']
                metric_values = [float(x[1]) for x in metric_values]
                time_points = [x * statistics_interval for x in range(0,len(metric_values))]
                all_values.append(metric_values)
                plt.plot(time_points,metric_values)    

            plt.xlabel("Time in Seconds")
            plt.ylabel("{0}".format(current_metric_type['y_label']))
            plt.title("{0}".format(current_metric_type['graph_title']))
            plt.autoscale()
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.savefig("{0}/{1}/plot{2}.png".format(results_dir_path,curr_time,current_metric_type['graph_title'].replace(" ", "").replace("'","")), bbox_inches='tight')
            plt.clf()
            if len(metric_data['data']['result']) > 1:
                all_values = np.array(all_values)
                percentiles = calculate_percentiles(all_metric_values, [50, 90, 99])
                plt.plot(time_points, percentiles[0], linestyle='--', color='black', label='50th percentile')
                plt.plot(time_points, percentiles[1], linestyle='--', color='red', label='90th percentile')
                plt.plot(time_points, percentiles[2], linestyle='--', color='blue', label='99th percentile')
                plt.legend(loc='upper right')
                plt.xlabel("Time in Seconds")
                plt.ylabel("{0}".format(current_metric_type['y_label']))
                plt.title("Procentiles for : {0}".format(current_metric_type['graph_title']))
                plt.savefig("{0}/{1}/procentiles_plot{2}.png".format(results_dir_path,curr_time,current_metric_type['graph_title'].replace(" ", "").replace("'","")), bbox_inches='tight')
                plt.clf()