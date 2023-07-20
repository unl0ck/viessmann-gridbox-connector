import json
import requests
# Opening JSON file
f = open('config.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
f.close() 

response = requests.post(data["urls"]["login"], data["login"])
#access_token = response.content["access_token"]
response_json = response.json()
id_token = response_json["id_token"]
response = requests.get(data["urls"]["gateways")
response_json = response.json()

print(response_json)
