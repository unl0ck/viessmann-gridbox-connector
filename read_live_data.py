from viessmann_gridbox_connector import GridboxConnector
from importlib.resources import files
import json

config_file = files('viessmann_gridbox_connector').joinpath('config.json')
with open(config_file, 'r') as file:
    data = json.load(file)
    data["login"]["username"] = "username"
    data["login"]["password"] = "password"
    connector = GridboxConnector(data)
    # Retrieve live data
    live_data = connector.retrieve_live_data()
    print(live_data)