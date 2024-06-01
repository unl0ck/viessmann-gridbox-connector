from viessmann_gridbox_connector import GridboxConnector
from importlib.resources import path
import json

with path('viessmann_gridbox_connector', 'config.json') as config_file:
    with open(config_file, 'r') as file:
        data = json.load(file)
        data["login"]["username"] = "username"
        data["login"]["password"] = "password"
        connector = GridboxConnector(data)
        # Retrieve live data
        live_data = connector.retrieve_live_data()
        print(live_data)