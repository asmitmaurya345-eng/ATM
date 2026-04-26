import json
import random
from datetime import datetime 
class Account():
    def __init__(self):
        acc_no=str(random.randrange(123456,999999))
        name=input("enter your name:")
        pin=int(input("create yout pin:"))
        while True:
            money=input("Enter amount you want to deposit:")
            if int(money)<=0 and money.isdigit():
                print("Please enter valid amount! (only integer)")
            else:
                break   
        with open ("database.json","a") as database
        today_date=str(datetime.now())[:10]
        full_info={acc_no:{"name":name,"pin":pin,"history":{today_date:money}}}
        database.dump({full_info})
        print("Your account have been created sucessfully>")
        database.close()
        