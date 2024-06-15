import sys
import json
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

statistics_interval = 1
metrics_path = sys.argv[1]

with open("metric_names.json") as metric_names_file:
    metric_types = json.load(metric_names_file)
    with open(metrics_path) as file:
        data = json.load(file)
        for i in range(len(data)):  
            current_metric_type = metric_types[i]
            metric_data = data[i]
            metric_data = json.loads(metric_data)
            metric_data = metric_data['data']['result'][0]['values']
            print(metric_data)
            metric_values = [float(x[1]) for x in metric_data]

            for i in range(len(metric_values)):
                if math.isnan(metric_values[i]):
                    metric_values[i] = 0
            print(type(metric_values[0]))

            time_points = [x * statistics_interval for x in range(0,len(metric_values))]
            print(metric_values)
        
            # formatter = ticker.ScalarFormatter(useOffset=False)
            # formatter.set_scientific(False)
            # plt.gca().yaxis.set_major_formatter(formatter)

            plt.plot(time_points,metric_values)
            plt.xlabel("Time in Seconds")
            plt.ylabel("{0}".format(current_metric_type['y_label']))
            plt.title("{0}".format(current_metric_type['graph_title']))
            plt.savefig("results/plot{0}.png".format(current_metric_type['graph_title'].replace(" ", "").replace("'","")), bbox_inches='tight')
                