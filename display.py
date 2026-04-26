import json
class Account():
    def __init__(self,):
        with open ("database.json","r") as database:
          self.data=json.load(database)
          database.close()
        while True:
            self.acc_no=input("Enter your account number:")
            if self.acc_no in self.data:
                per_info=self.data[self.acc_no]
                print("Acount number:",self.acc_no)
                print("Acount Holder Name:",per_info["name"])
                print("Balance:",per_info["balance"])
                break
            else:
                print("Enter correct account number!")
        self.c=input("press enter to exit :)")
