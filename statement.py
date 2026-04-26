import json
class Account_History():
    def __init__(self):
        while True:
            self.acc_no=input("Enter yout account number:")
            with open ("database.json","r") as database:
                self.data=json.load(database)
            if self.acc_no in self.data:
                self.per_info=self.data[self.acc_no]
                self.statement=self.per_info["history"]
                for x,y in self.statement.items():
                    print("Date",x,"Amount",y)
                self.c=input("press enter to exit :)")
            else:
                print("Please enter correct account number!")