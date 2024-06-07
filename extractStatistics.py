import requests
import sys


start_time = sys.argv[1]
end_time = sys.argv[2]

tick_time_query = "http://localhost:9090/api/v1/query_range?query=net_minecraft_server_Server_averageTickTime&start={1}.999Z&end={2}.000Z&step=5s".format(start_time,end_time)

tick_time_response = requests.get(tick_time_query)

with open("metrics.json",'w') as file:
    file.write(tick_time_response.text)



print(tick_time_response.text)
print(type(tick_time_response))