from gridbox_connector import GridboxConnector

config = {
    "urls": {
        "login": "https://example.com/login",
        "gateways": "https://example.com/gateways",
        "live": "https://example.com/live/{}",
    },
    "login": {"username": "your_username", "password": "your_password"},
}

connector = GridboxConnector(config)

# Retrieve live data
live_data = connector.retrieve_live_data()
print(live_data)
