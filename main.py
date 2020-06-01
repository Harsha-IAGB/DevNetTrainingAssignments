import accounts_data
import dnac_devices_data
import json

print(json.dumps(accounts_data.get_accounts_data(), indent=4))
print(json.dumps(dnac_devices_data.get_dnac_device_data(), indent=4))