import requests
import time
class GridboxConnector:
    id_token = ""

    def __init__(self,config):
        self.login_url = config["urls"]["login"]
        self.login_body = config["login"]
        self.gateway_url = config["urls"]["gateways"]
        self.live_url = config["urls"]["live"]
        self.init_auth()
    
    def init_auth(self):
        self.get_token()
        self.generate_header()
        self.get_gateway_id()

    def get_token(self):
        response = requests.post(self.login_url, self.login_body)
        response_json = response.json()
        print(response_json)
        if "id_token" in response_json:
            self.id_token  = response_json["id_token"]
        else:
            print("token not found")
            print(response_json)
            time.wait(60)
            self.get_token()
       
    def generate_header(self):
        self.headers = {"Authorization": "Bearer {}".format(self.id_token)}

    def get_gateway_id(self):
        response = requests.get(self.gateway_url,headers=self.headers)
        response_json = response.json()
        gateway = response_json[0]
        self.gateway_id = gateway["system"]["id"]

    def retrieve_live_data(self):
        response = requests.get(self.live_url.format(self.gateway_id),headers=self.headers)
        if response.status_code == 200:
            response_json = response.json()
            #print(response_json)
            return response_json
        else:
            print("Status Code {}".format(response.status_code))
            print("Response {}".format(response.json()))
            time.sleep(60)
            self.init_auth()
            return self.retrieve_live_data()
