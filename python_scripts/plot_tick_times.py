import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys

results_dir_path = sys.argv[1]
timestamp = sys.argv[2]
ticktime_path = sys.argv[3]

start_time = float(sys.argv[4])
end_time = float(sys.argv[5])


print("start_time: ",start_time,"\n end_time: ",end_time)
print("start_time: ",type(start_time),"\n end_time: ",type(end_time))


with open(ticktime_path) as file:
    data = json.load(file)  

    tick_times = data[0]
    time_stamps = data[1]

    start = time_stamps[0]
    start_index = 0

    print("start extracted from time_stamps: ",start)
    print("start extracted from time stamps: ",type(start))
    

    end_index = len(time_stamps) -1
    
    for i in range(len(time_stamps)):
        if float(time_stamps[i]) >= start_time:
            start_index = i
            start = time_stamps[i]
            break
    for i in range((len(time_stamps) -1),0,-1):
        if float(time_stamps[i]) <= end_time:
            end_index = i
            break



    time_stamps = time_stamps[start_index:end_index + 1]

    with open("plot.log","w+") as log:
        str = (
        f"Time begin: {time_stamps[0]}\n"
        f"Time end: {time_stamps[-1]}\n"
        f"Time diff: {time_stamps[-1] - time_stamps[0]}\n"
        f"Type of time: {type(time_stamps[0])}\n"
        f"Facts: {start_time} - {end_time}\n"
        f"Time diff between start and end: {end_time - start_time}"
        )
        log.write(str)

    time_points = [(t - start)/1000000000 for t in time_stamps]
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(time_points,tick_times)      
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
