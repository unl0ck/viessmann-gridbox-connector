# Viessmann Gridbox Connector
**This is not an official Viessmann library**

a GridboxConnector Lib to fetch your Data from the Cloud.
It is using the same Rest-API like the Dashboard and the App.

## Installation
Set your email and password in the config.json. 
Use your Login Data from the App or from https://mygridbox.viessmann.com/login

### Setup the python environment and install all dependencies

```script shell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
### Example Output
```script json
{
    "consumption": 496,
    "directConsumption": 413,
    "directConsumptionEV": 0,
    "directConsumptionHeatPump": 0,
    "directConsumptionHeater": 0,
    "directConsumptionHousehold": 413,
    "directConsumptionRate": 1,
    "grid": 83,
    "gridMeterReadingNegative": 4318200000,
    "gridMeterReadingPositive": 14499360000,
    "measuredAt": "2023-08-04T11:29:43Z",
    "photovoltaic": 413,
    "production": 413,
    "selfConsumption": 413,
    "selfConsumptionRate": 1,
    "selfSufficiencyRate": 0.8326612903225806,
    "selfSupply": 413,
    "totalConsumption": 496
}
```

# Usage
```python
from gridbox_connector import GridboxConnector

# Initialize the connector with your configuration
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

```
# Configuration
You need to provide a configuration dictionary with the following keys:

urls: Dictionary containing endpoint URLs.
login: Dictionary containing login credentials.

# Dependencies
requests
# Contributing
If you'd like to contribute to viessmann-gridbox-connector, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and write tests if possible.
Run tests and ensure they pass.
Submit a pull request.


# License

This project is licensed under the MIT License - see the LICENSE file for details.
