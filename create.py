import json
import random
from datetime import datetime 
class Account():
    def __init__(self):
        acc_no=str(random.randrange(123456,999999))
        name=input("enter your name:")
        pin=int(input("create yout pin:"))
        while True:
            money=float(input("Enter amount you wat to deposit"))
            if money<=0:
                print("Please enter valid amount")
            else:
                break   
        with open ("database.json","a") as database
        today_date=str(datetime.now())[:10]
        full_info={acc_no:{"name":name,"pin":pin,"history":{today_date:money}}}
        database.dump({full_info})