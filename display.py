import json
class Account():
    def __init__(self,acc_no):
        with open ("database.json","r") as database
        data=json.load(database)
        if self.acc_no in data:
            per_info=data[acc_no]
            print("Acount number;",self.acc_no)
            print("Acount Holder Name;",per_info["name"])
            print("Balance:",per_info[balance])
            database.close()
