import json
from datetime import datetime
class Deposit():
    def __init__(self):
        with open ("database.json","r") as database:
            self.data=json.load(database)
            while True:
                self.Acc_no=input("Enter your account number:")
                if self.Acc_no in self.data:
                    self.per_info=self.data[self.Acc_no]
                    while True:
                        try:
                            self.pin=int(input("Enter your pin:"))
                            if self.pin==self.per_info["pin"]:
                                print("pin accepted")
                                while True:
                                    try:
                                        self.money=int(input("Enter amount you want to deposit:"))
                                        if self.money <= 0:
                                            print("Please enter a positive amount!")
                                            continue
                                        self.per_info["balance"]+=self.money
                                        self.history=self.per_info["history"]
                                        self.today=str(datetime.now())[:10]
                                        if self.today in self.history:
                                            self.history[self.today]+=self.money
                                        else:
                                            self.history[self.today]=self.money
                                        with open ("database.json","w") as database:
                                            json.dump(self.data,database,indent=4)
                                            print(f"Amount of ₹{self.money} has been successfully deposited.")
                                            self.c=input("press enter to exit :)")
                                            return
                                    except ValueError:
                                        print("Enter valid amount! (integer only)")
                                        continue
                            else:
                                print("pin incorrect try again!")
                                continue
                        except ValueError:
                            print("Enter correct pin!")
                            continue
                else:
                    print("Enter correct account number!")
                    continue