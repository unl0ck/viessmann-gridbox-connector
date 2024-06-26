import requests
import time
import logging
import os

class GridboxConnector:
    id_token: str = ""
    gateways: list[str] = []

    def __init__(self, config):
        self.init_logging()
        self.login_url = config["urls"]["login"]
        self.login_body = config["login"]
        self.gateway_url = config["urls"]["gateways"]
        self.live_url = config["urls"]["live"]
        self.init_auth()

    def init_logging(self):
        self.logger = logging.getLogger(__name__)
        loglevel = os.getenv('LOG_LEVEL', 'DEBUG')  # Default to DEBUG if LOGLEVEL is not set
        self.logger.setLevel(logging.getLevelName(loglevel))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
    
    def init_auth(self):
        self.get_token()
        self.generate_header()
        self.get_gateway_id()

    def get_token(self):
        try:
            response = requests.post(self.login_url, self.login_body)
            response_json = response.json()
            self.logger.debug(response_json)
            if "id_token" in response_json:
                self.id_token = response_json["id_token"]
            else:
                self.logger.warn("token not found")
                print(response_json)
                time.sleep(60)
                self.get_token()
        except Exception as e:
            self.logger.error(e)
            time.sleep(60)
            self.get_token()

    def generate_header(self):
        self.headers = {"Authorization": "Bearer {}".format(self.id_token)}

    def get_gateway_id(self):
        self.gateways.clear()
        try:
            response = requests.get(self.gateway_url, headers=self.headers)
            response_json = response.json()
            for gateway in response_json:
                self.gateways.append(gateway["system"]["id"])
        except Exception as e:
            self.logger.error(e)
            time.sleep(60)
            self.get_gateway_id()

    def retrieve_live_data(self):
        responses = []
        for id in self.gateways:
            try:
                response = requests.get(self.live_url.format(id), headers=self.headers)
                if response.status_code == 200:
                    response_json = response.json()
                    responses.append(response_json)
                    # print(response_json)
                else:
                    self.logger.warn("Status Code {}".format(response.status_code))
                    self.logger.warn("Response {}".format(response.json()))
            except Exception as e:
                self.logger.error(e)
        return responses
