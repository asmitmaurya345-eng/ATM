import json
import random
from datetime import datetime 
class Creat_Account():
    def __init__(self):
        self.acc_no=str(random.randrange(123456,999999))
        self.name=input("enter your name:")
        self.pin=int(input("create yout pin:"))
        while True:
            self.money=input("Enter amount you want to deposit:")
            if int(self.money)<=0 and self.money.isdigit():
                print("Please enter valid amount! (only integer)")
            else:
                break   
        with open ("database.json","a") as database
        today_date=str(datetime.now())[:10]
        self.full_info={self.acc_no:{"name":self.name,"pin":self.pin,"history":{today_date:self.money}}}
        database.dump({self.full_info})
        print("Your account have been created sucessfully>")
        database.close()