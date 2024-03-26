from gridbox_connector import GridboxConnector
import json

with open('config.json', 'r') as file:
    data = json.load(file)
    connector = GridboxConnector(data)
    # Retrieve live data
    live_data = connector.retrieve_live_data()
    print(live_data)
