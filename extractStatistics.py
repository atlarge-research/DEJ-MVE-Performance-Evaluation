import requests
import sys


start_time = sys.argv[1]
end_time = sys.argv[2]

tick_time_query = "http://localhost:9090/api/v1/query_range?query=net_minecraft_server_Server_averageTickTime&start={0}.999Z&end={1}.000Z&step=1s".format(start_time,end_time)
tick_time_response = requests.get(tick_time_query)


with open("metrics.json",'w') as file:
    file.write(tick_time_response.text)
