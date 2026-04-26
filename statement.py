import json
class Account():
    def __init__(self):
        while True:
            self.acc_no=input("Enter yout account number:")
            with open ("database.json","a") as database
            self.data=json.load(database)
            self.per_info=self.data[self.acc_no]
            