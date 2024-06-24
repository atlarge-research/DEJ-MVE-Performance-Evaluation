import sys
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

statistics_interval = 1
metrics_path = sys.argv[1]
metric_names_path = sys.argv[2]
results_dir_path = sys.argv[3]
timestamp = sys.argv[4]


with open(metric_names_path) as metric_names_file:
    metric_types = json.load(metric_names_file)
    with open(metrics_path) as file:
        data = json.load(file)
        
        for i in range(len(data)):  
            current_metric_type = metric_types[i]
            metric_data = data[i]
            metric_data = json.loads(metric_data)
            fig, ax = plt.subplots(figsize=(10, 6))
            for metric in metric_data['data']['result']:
                metric_values = metric['values']
                metric_values = [float(x[1]) for x in metric_values]
                ax.plot(metric_values)      

            ax.xaxis.set_major_locator(ticker.MultipleLocator(base=10))
            ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=5))
            ax.set_xlabel("Time[s]")
            ax.set_ylabel("{0}".format(current_metric_type['y_label']))
            plt.tight_layout()
            plt.margins(0)
            ax.grid(True,which="both",linestyle='--', alpha=0.5)
            plt.savefig("{0}/{1}/plot{2}.pdf".format(results_dir_path,timestamp,current_metric_type['graph_title'].replace(" ", "")), bbox_inches='tight')
            plt.savefig("{0}/{1}/plot{2}.png".format(results_dir_path,timestamp,current_metric_type['graph_title'].replace(" ", "")), bbox_inches='tight')
            plt.clf()