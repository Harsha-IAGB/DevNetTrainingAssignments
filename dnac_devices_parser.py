import json

def get_dnac_device_data():
    dnac_device_data = json.load(open("data/dnac_devices.json", 'r'))
    processed_device_data = []
    for dnac_device in dnac_device_data['response']:
        temp = {}
        temp['id'] = dnac_device['id']
        temp['family'] = dnac_device['family']
        temp['softwareType'] = dnac_device['softwareType']
        temp['type'] = dnac_device['type']
        temp['managementIpAddress'] = dnac_device['managementIpAddress']
        processed_device_data.append(temp)
    return processed_device_data
