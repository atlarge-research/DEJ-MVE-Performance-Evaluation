import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

results_dir_path = sys.argv[1]
timestamp = sys.argv[2]
ticktime_path = sys.argv[3]



with open(ticktime_path) as file:
    data = json.load(file)    
    metric_data = json.loads(metric_data)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(metric_data)      
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=60))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=30))
    ax.set_xlabel("Time[s]")
    ax.set_ylabel("Average Tick Time[MS]")
    plt.tight_layout()
    plt.margins(0)
    ax.grid(True,which="both",linestyle='--', alpha=0.5)
    plt.savefig("{0}/{1}/jolokia_tick_time.pdf".format(results_dir_path,timestamp,current_metric_type['graph_title'].replace(" ", "")), bbox_inches='tight')
    plt.savefig("{0}/{1}/jolokia_tick_time.png".format(results_dir_path,timestamp,current_metric_type['graph_title'].replace(" ", "")), bbox_inches='tight')
    plt.clf()