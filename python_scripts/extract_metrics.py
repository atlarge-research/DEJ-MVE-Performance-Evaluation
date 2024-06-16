import requests
import sys
import json

start_time = sys.argv[1]
end_time = sys.argv[2]


def do_query(metric_name):
   query = "http://localhost:9090/api/v1/query_range?query={0}&start={1}.999Z&end={2}.000Z&step=1s".format(metric_name,start_time,end_time)
   return requests.get(query) 


with open("metric_names.json") as metric_names_file:
   metric_types = json.load(metric_names_file)
   query_responses = [do_query(metric_name=metric['metric_name']).text for metric in metric_types]
   with open("metrics.json",'w') as file:
      json.dump(query_responses,file)







