import json
from datetime import datetime
class Withdraw():
    def __init__(self):
        self.Acc_no=input("Enter your accouunt number:")
        with open ("database.json","r") as database:
            self.data=json.load(database)
            while True:
                if self.Acc_no in self.data:
                    self.per_info=self.data[self.Acc_no]
                    while True:
                        while True:
                            try:
                                self.money=int(input("Enter amount you want to withdraw:"))
                                break
                            except ValueError:
                                print("Enter valid amount!")
                        if self.money>self.per_info["balance"]:
                            self.per_info["balance"]-=self.money
                            break
                        else:
                            print("Enter valid amount")
                    self.history=self.per_info["history"]
                    self.today=str(datetime.now())[:10]
                    if self.today in self.history:
                        self.history[self.today]-=self.money
                    else:
                        self.history[self.today]=self.money*-1
                    database.close()
                    break
                else:
                    print("Enter correct account number!")
        with open ("database.json","w") as database:
            json.dump(self.data,database)
            database.close()