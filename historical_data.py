from viessmann_gridbox_connector import GridboxConnector
from importlib.resources import files
from datetime import datetime, timezone, timedelta
import json
import time
import urllib.parse



now = datetime.now(timezone(timedelta(hours=1)))
now = now.replace(hour=0, minute=0, second=0, microsecond=0)

today = now.isoformat()
tomorrow = now + timedelta(days=1)

loop = False
config_file = files('viessmann_gridbox_connector').joinpath('config.json')
with open(config_file, 'r') as file:
    data = json.load(file)
    data["login"]["username"] = "username"
    data["login"]["password"] = "password"
    connector = GridboxConnector(data)
    # Retrieve live data
    historical_data = connector.retrieve_historical_data(start=today, end=tomorrow.isoformat())
    print(historical_data)
    while loop:
        historical_data = connector.retrieve_historical_data(start=today, end=tomorrow.isoformat())
        print(historical_data)
        time.sleep(60)