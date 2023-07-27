import json
import time
import os
from GridboxConnector import GridboxConnector
if __name__ == '__main__':
    f = open(os.path.dirname(__file__)+ os.sep + '..' + os.sep + '..' + os.sep + 'config.json')
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    f.close()
    while True:
        print(GridboxConnector(data).retrieve_live_data())
        time.sleep(300)