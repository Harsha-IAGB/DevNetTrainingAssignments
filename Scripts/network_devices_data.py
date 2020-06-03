import requests, json
from requests.auth import HTTPBasicAuth

class DevicesAPI():
    def __init__(self, username, password):
        self.username = username
        self.password = password

        token = self.login()

        self.device_data = self.get_device_data_from_API(token)

    def get_device_data_from_API(self, token):
        headers = {
            'x-auth-token':token
        }
        response = requests.get("https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device", headers=headers)
        return response.json()

    def login(self):
        response = requests.post('https://sandboxdnac2.cisco.com/api/system/v1/auth/token', auth=HTTPBasicAuth(self.username, self.password))
        return response.json()['Token']

    def get_device_data(self):
        return self.device_data