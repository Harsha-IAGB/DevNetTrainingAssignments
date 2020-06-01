from any_parser import Parser

def get_accounts_data():
    accounts = {}
    # parsing "db.json"
    acc1to3 = Parser("data/db.json").get_parsed_data()
    accounts.update(acc1to3)

    # parsing db.xml
    acc4to6 = Parser("data/db.xml").get_parsed_data()
    accounts.update(acc4to6)

    # parsing db.yml
    acc7to9 = Parser("data/db.yml").get_parsed_data()
    accounts.update(acc7to9)
    return accounts

if __name__ == "__main__":
    print(get_accounts_data())