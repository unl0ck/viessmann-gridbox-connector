# Viessmann Gridbox Connector
**This is not an official Viessmann library**

a GridboxConnector Lib to fetch your Data from the Cloud.
It is using the same Rest-API like the Dashboard and the App.
## How-To use
Set your email and password in the config.json. 
Use your Login Data from the App or from https://mygridbox.viessmann.com/login

```script shell
pip install -r requirements.txt
python read_live_data.py
```

## Example Output
These Data will get
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

# To-Do
* Create a pypi lib
* Better Documentation
