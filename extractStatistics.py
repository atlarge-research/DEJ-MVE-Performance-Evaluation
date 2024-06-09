import requests
import sys
import json

start_time = sys.argv[1]
end_time = sys.argv[2]

metric_names = ["net_minecraft_server_Server_averageTickTime"]

def do_query(metric_name):

   query = "http://localhost:9090/api/v1/query_range?query={0}&start={1}.999Z&end={2}.000Z&step=5s".format(metric_name,start_time,end_time)
   return requests.get(query) 


query_responses = [do_query(metric_name=name).text for name in metric_names]


with open("metrics.json",'w') as file:
    json.dump(query_responses,file)
