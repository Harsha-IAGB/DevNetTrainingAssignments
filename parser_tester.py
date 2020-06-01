import unittest
from any_parser import Parser

class ParserTestMethods(unittest.TestCase):
    def test_json_parser(self):
        test_json_file = "data/db.json"
        expected_output = {'ACCT100': {'paid': 60, 'due': 100}, 'ACCT200': {'paid': 70, 'due': 60}, 'ACCT300': {'paid': 0, 'due': 0}}
        actual_output = Parser(test_json_file).get_parsed_data()
        self.assertEqual(actual_output, expected_output)

    def test_xml_parser(self):
        test_xml_file = "data/db.xml"
        expected_output = {'ACCT400': {'@extra': 'fun', 'paid': '600', 'due': '10000'}, 'ACCT500': {'paid': '70', 'due': '40'}, 'ACCT600': {'paid': '0', 'due': '0'}}
        actual_output = Parser(test_xml_file).get_parsed_data()
        self.assertEqual(actual_output, expected_output)

    def test_yaml_parser(self):
        test_yaml_file = "data/db.yml"
        expected_output = { 'ACCT700': {'paid': 60, 'due': 100}, 'ACCT800': {'paid': 70, 'due': 60}, 'ACCT900': {'paid': 0, 'due': 0}}
        actual_output = Parser(test_yaml_file).get_parsed_data()
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()