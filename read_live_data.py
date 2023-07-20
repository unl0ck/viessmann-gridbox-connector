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
print(response_json)
id_token = response_json["id_token"]
gateway_url = data["urls"]["gateways"]

headers = {"Authorization": "Bearer {}".format(id_token)}
response = requests.get(gateway_url,headers=headers)
response_json = response.json()
gateway = response_json[0]
gateway_id = gateway["system"]["id"]
live_url = data["urls"]["live"]
live_url = live_url.format(gateway_id)
response = requests.get(live_url,headers=headers)
response_json = response.json()
print(response_json)
