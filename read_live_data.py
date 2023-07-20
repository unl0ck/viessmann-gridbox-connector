import json
import requests
# Opening JSON file
f = open('config.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
f.close() 
# Iterating through the json
# list
for i in data:
    print(i)
  
response = requests.post(data["token"], data["login"])
#access_token = response.content["access_token"]
response_json = response.json()
print(response_json)
