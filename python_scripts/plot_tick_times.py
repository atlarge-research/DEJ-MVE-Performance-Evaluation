import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys

results_dir_path = sys.argv[1]
timestamp = sys.argv[2]
ticktime_path = sys.argv[3]



with open(ticktime_path) as file:
    data = json.load(file)  

    tick_times = data[0]
    time_stamps = data[1]
    start = time_stamps[0]
    time_points = [int(t - start) for t in time_stamps]
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(time_points,tick_times)      
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=10))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=5))
    ax.set_ylim(ymin=0)

    ax.set_xlabel("Time[s]")
    ax.set_ylabel("Average Tick Time[MS]")
    plt.tight_layout()
    plt.margins(0)
    ax.grid(True,which="both",linestyle='--', alpha=0.5)
    plt.savefig("{0}/{1}/jolokia_tick_time.pdf".format(results_dir_path,timestamp), bbox_inches='tight')
    plt.savefig("{0}/{1}/jolokia_tick_time.png".format(results_dir_path,timestamp), bbox_inches='tight')
    plt.clf()
