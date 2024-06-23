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
    print(len(tick_times))
    print(len(time_stamps))

    start = time_stamps[0]

    time_points = [(t - start)/1000000000 for t in time_stamps]
    print(time_points[0])
    print(time_points[-1])
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(tick_times,time_points)      
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=60))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=30))
    ax.set_xlabel("Time[s]")
    ax.set_ylabel("Average Tick Time[MS]")
    plt.tight_layout()
    plt.margins(0)
    ax.grid(True,which="both",linestyle='--', alpha=0.5)
    plt.savefig("{0}/{1}/jolokia_tick_time.pdf".format(results_dir_path,timestamp), bbox_inches='tight')
    plt.savefig("{0}/{1}/jolokia_tick_time.png".format(results_dir_path,timestamp), bbox_inches='tight')
    plt.clf()
