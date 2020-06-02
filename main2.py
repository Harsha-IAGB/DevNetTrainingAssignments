import json
from network_devices_data import DevicesAPI
from generic_parser import Parser

tok = DevicesAPI('dnacdev', 'D3v93T@wK!').get_device_data()
print(json.dumps(tok, indent=2))

with open("Output/devices_from_api.json", 'w') as output_file:
    json.dump(tok, output_file)