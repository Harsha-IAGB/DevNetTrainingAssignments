import unittest, json
from network_devices_data import DevicesAPI
from generic_parser import Parser

class APITesterMethods(unittest.TestCase):

    def test_get_data(self):
        self.maxDiff = None
        username = "dnacdev"
        password = "D3v93T@wK!"
        expected_output = json.dumps(Parser("../Output/devices_from_api.json").get_parsed_data())
        actual_output = json.dumps(DevicesAPI(username, password).get_device_data())
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()