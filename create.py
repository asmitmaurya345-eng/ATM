import json
import random
from datetime import datetime 
class Creat_Account():
    def __init__(self):
        with open ("database.json","r") as database:
            self.data=json.load(database)
            database.close()
        while True:
            self.acc_no=str(random.randrange(123456,999999))
            if self.acc_no not in self.data:
                break
        self.name=input("enter your name:")
        self.pin=int(input("create yout pin:"))
        while True:
            self.money=input("Enter amount you want to deposit:")
            if int(self.money)<=0 and self.money.isdigit():
                print("Please enter valid amount! (only integer)")
            else:
                break   
        today_date=str(datetime.now())[:10]
        self.full_info={"name":self.name,"pin":self.pin,"balance":self.money,"history":{today_date:self.money}}
        self.data[self.acc_no]=self.full_info
        with open ("database.json","w") as database:
            json.dump(self.data,database,indent=4)
            print("Your account have been created sucessfully :)")
            print("Your account number is:",self.acc_no)
            database.close()
