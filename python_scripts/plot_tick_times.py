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

with open(ticktime_path) as file:
    data = json.load(file)  

    tick_times = data[0]
    time_stamps = data[1]

    start = time_stamps[0]
    start_index = 0
    allowance = 3
    end_index = len(time_stamps) -1
    
    for i in range(len(time_stamps)):
        print("Time_stamp: ",time_stamps[i], "start_time: ", start_time)
        print("Diff: ",time_stamps[i]-start_time)
        print("__________________________________")
        if abs(float(time_stamps[i])- start_time) <= allowance:
            start_index = i
            start = time_stamps[i]
            break
    for i in range((len(time_stamps) -1),0,-1):
        print("Time_stamp: ",time_stamps[i], "end_time: ", end_time)
        print("Diff: ",time_stamps[i]-end_time)
        print("__________________________________")
        if abs(float(time_stamps[i]) - end_time) <= allowance:
            end_index = i
            break

    time_stamps = time_stamps[start_index:end_index + 1]
    tick_times = tick_times[start_index:end_index+1]
    time_points = [int(t - start) for t in time_stamps]
    print(time_points)
    fig, ax = plt.subplots(figsize=(10, 6))

    with open("plot.log","w+") as log:
        str = (
        f"Time begin: {time_stamps[0]}\n"
        f"Time end: {time_stamps[-1]}\n"
        f"Time diff: {time_stamps[-1] - time_stamps[0]}\n"
        f"Type of time: {type(time_stamps[0])}\n"
        f"Facts: {start_time} - {end_time}\n"
        f"Time diff between start and end: {end_time - start_time} \n"
        f"First time_point: {time_points[0]} last: {time_points[-1]} diff: {time_points[0]-time_points[-1]} \n"
        )
        log.write(str)





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
