import sys
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as plt_tick

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
            tick_times = [float(x[1]) for x in metric_data]            
            time_points = [x * statistics_interval for x in range(0,len(tick_times))]
            fig, ax = plt.subplots()
            ax.plot(time_points,tick_times)
            # ax.ticklabel_format(useOffset=False, style='plain')
            ax.get_yaxis().set_major_formatter(plt_tick.FuncFormatter(lambda x, p: format(int(x), ',')))

            plt.xlabel("Time in Seconds")
            plt.ylabel("{0}".format(current_metric_type['y_label']))
            plt.title("{0}".format(current_metric_type['graph_title']))
            fig.savefig("results/plot{0}.png".format(current_metric_type['graph_title'].replace(" ", "").replace("'","")), bbox_inches='tight')
