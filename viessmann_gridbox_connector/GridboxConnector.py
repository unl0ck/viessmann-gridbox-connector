import requests
import time
import logging
import os
from authlib.integrations.requests_client import OAuth2Session

class GridboxConnector:
    id_token: str = ""
    gateways: list[str] = []
    token: dict = {}
    client: OAuth2Session = None
    config: dict = {}
    username: str = ""
    password: str = ""

    def __init__(self, config):
        self.init_logging()
        self.config = config
        self.login_url = config["urls"]["login"]
        self.login_body = config["login"]
        self.gateway_url = config["urls"]["gateways"]
        self.live_url = config["urls"]["live"]
        self.historical_url = config["urls"]["historical"]
        self.username = os.getenv('USERNAME', self.login_body["username"])
        self.password = os.getenv('PASSWORD', self.login_body["password"])
        self.init_auth()

    def init_logging(self):
        self.logger = logging.getLogger(__name__)
        loglevel = os.getenv('LOG_LEVEL', 'INFO')
        self.logger.setLevel(logging.getLevelName(loglevel))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    
    def get_new_token(self):
        self.token = self.client.fetch_token(
            self.login_url,
            username=self.login_body["username"],
            password=self.login_body["password"],
            grant_type=self.login_body['grant_type'],
            audience=self.login_body['audience'],
            realm=self.login_body['realm'],
            scope=self.login_body['scope']
        )
        self.logger.debug(f"Token expires at {self.token['expires_at']}")
    
    # Funktion zum Überprüfen und Erneuern des Tokens
    def ensure_valid_token(self):
        # Prüfe, ob das Token abgelaufen ist
        expires_at = self.token.get('expires_at')
        if expires_at is None or expires_at < time.time():
            self.logger.info("Token ist abgelaufen oder nicht vorhanden, erneuern...")
            self.get_new_token()  

    def get_header(self):
        self.ensure_valid_token()
        return {"Authorization": f'Bearer {self.token["id_token"]}'}    
    
    def init_auth(self):
        client_id = self.login_body["client_id"]
        client_secret = self.login_body["client_secret"]
        self.client = OAuth2Session(client_id, client_secret, scope=self.login_body["scope"])
        self.get_new_token()
        self.get_gateway_id()

    def get_gateway_id(self):
        self.gateways.clear()
        try:
            response = requests.get(self.gateway_url, headers=self.get_header())
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
                response = requests.get(self.live_url.format(id), headers=self.get_header())
                if response.status_code == 200:
                    response_json = response.json()
                    responses.append(response_json)
                    # print(response_json)
                else:
                    self.logger.warning("Status Code {}".format(response.status_code))
                    self.logger.warning("Response {}".format(response.json()))
            except Exception as e:
                self.logger.error(e)
        return responses
    
    def retrieve_historical_data(self, start, end, resolution='15m'):
        responses = []
        
        for id in self.gateways:
            interval = f"{start}/{end}"
            import urllib.parse
            encoded_string = urllib.parse.quote(interval)
            self.historical_url_created = self.historical_url.format(id, encoded_string, resolution)
            try:
                response = requests.get(self.historical_url_created, headers=self.get_header())
                if response.status_code == 200:
                    response_json = response.json()
                    responses.append(response_json)
                    # print(response_json)
                else:
                    self.logger.warning("Requested url {}".format(self.historical_url_created))
                    self.logger.warning("Status Code {}".format(response.status_code))
                    self.logger.warning("Response {}".format(response.json()))
            except Exception as e:
                self.logger.error(e)
        return responses