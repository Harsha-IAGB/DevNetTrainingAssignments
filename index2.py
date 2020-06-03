#!/usr/bin/python3
print("Content-Type:text/html")
print("")

import cgi,cgitb
cgitb.enable() # Enable debugging
print("<h1>Below is the execution output of the script</h1>")
print("------------------------------------<br>")

##-------PASTE YOUR SCRIPT BELOW---------#######

import json
from Scripts.generic_parser import Parser
from Scripts.network_devices_data import DevicesAPI

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

def main():
    """
    Execution begins here.
    """

    dnac_devices = DnacDevices()
    local_data = dnac_devices.get_local_data("data/dnac_devices.json")
    print("<h3>Local Data...</h3>")
    print("<p>")
    print(json.dumps(local_data, indent=2))
    print("</p>")
    print("<br></br>")
    remote_data = dnac_devices.get_server_data('dnacdev', 'D3v93T@wK!')
    print("<h3>Server Data Obtained through API...</h3>")
    print("<p>")
    print(json.dumps(remote_data, indent=2))
    print("</p>")
main()