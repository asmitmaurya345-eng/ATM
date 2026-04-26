import json
from datetime import datetime
class Deposit():
    def __init__(self):
        self.Acc_no=input("Enter your accouunt number:")
        with open ("database.json","a") as database
        self.data=json.load(database)
        if self.Acc_no in self.data:
            self.per_info=self.data[self.Acc_no]
            