import accounts_data_parser
import dnac_devices_parser
import json

print(json.dumps(accounts_data_parser.get_accounts_data(), indent=4))
print(json.dumps(dnac_devices_parser.get_dnac_device_data(), indent=4))