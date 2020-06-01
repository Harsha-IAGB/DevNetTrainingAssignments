import json, xmltodict, yaml

def get_accounts_data():
    accounts = {}
    # parsing "db.json"
    with open("data/db.json", 'r') as json_file:
        acc1to3 = json.load(json_file)
        accounts.update(acc1to3)

    # parsing db.xml
    with open("data/db.xml", 'r') as xml_file:
        acc4to6 = json.loads(json.dumps(xmltodict.parse(xml_file.read())))
        # print(type(acc4to6['root']))
        accounts.update(acc4to6['root'])

    # parsing db.yml
    with open("data/db.yml", 'r') as yaml_file:
        acc7to9 = yaml.safe_load(yaml_file)
        accounts.update(acc7to9)
    return accounts