import json
from generic_parser import Parser
from network_devices_data import DevicesAPI

class DnacDevices():
    def __init__(self):
        self.remote_data = None
        self.local_data = None

    def get_server_data(self, username, password):
        if self.remote_data is None:
            self.remote_data = DevicesAPI(username, password).get_device_data()
        return self.remote_data

    def get_local_data(self, filepath):
        if self.local_data is None:
            dnac_device_data = Parser(filepath).get_parsed_data()
            processed_device_data = []
            for dnac_device in dnac_device_data['response']:
                temp = {}
                temp['id'] = dnac_device['id']
                temp['family'] = dnac_device['family']
                temp['softwareType'] = dnac_device['softwareType']
                temp['type'] = dnac_device['type']
                temp['managementIpAddress'] = dnac_device['managementIpAddress']
                processed_device_data.append(temp)
            self.local_data = processed_device_data
        return self.local_data

if __name__ == "__main__":
    dnac_devices = DnacDevices()
    local_data = dnac_devices.get_local_data("../data/dnac_devices.json")
    print(json.dumps(local_data, indent=2))
    remote_data = dnac_devices.get_server_data('dnacdev', 'D3v93T@wK!')
    print(json.dumps(remote_data, indent=2))