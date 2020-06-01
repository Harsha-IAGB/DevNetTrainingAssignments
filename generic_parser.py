import json, xmltodict, yaml

class Parser():
    def __init__(self, filepath):
        self.filepath = filepath
        self.parsed_data = None

        if '.json' in filepath:
            self.parse_json()
        elif '.xml' in filepath:
            self.parse_xml()
        elif '.yml' in filepath:
            self.parse_yaml()

    def parse_json(self):
        with open(self.filepath, 'r') as json_file:
            self.parsed_data = json.load(json_file)
    
    def parse_xml(self):
        with open(self.filepath, 'r') as xml_file:
            temp = json.loads(json.dumps(xmltodict.parse(xml_file.read())))
            self.parsed_data = temp['root']
    
    def parse_yaml(self):
        with open(self.filepath, 'r') as yaml_file:
            temp = yaml.safe_load(yaml_file)
            self.parsed_data = temp
    
    def get_parsed_data(self):
        return self.parsed_data