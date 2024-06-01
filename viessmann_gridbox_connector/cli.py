import argparse
from viessmann_gridbox_connector import GridboxConnector
from importlib.resources import files
import json

def retrieve_live_data(username, password):
    config_file = files('viessmann_gridbox_connector').joinpath('config.json')
    with open(config_file, 'r') as file:
        data = json.load(file)
        data["login"]["username"] = username
        data["login"]["password"] = password
        connector = GridboxConnector(data)
        # Retrieve live data
        live_data = connector.retrieve_live_data()
        return live_data

def main():
    parser = argparse.ArgumentParser(description='Retrieve live data from Viessmann Gridbox.')
    parser.add_argument('-u', '--username', required=True, help='The username to use.')
    parser.add_argument('-p', '--password', required=True, help='The password to use.')
    args = parser.parse_args()

    live_data = retrieve_live_data(args.username, args.password)
    print(live_data)

if __name__ == '__main__':
    main()