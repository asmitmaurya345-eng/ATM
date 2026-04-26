from display import Account
from create import Creat_Account
from statement import Account_History
from deposit import Deposit
from withdraw import Withdraw
while True:
    print("\n" + "="*30)
    print("     ATM MANAGEMENT SYSTEM")
    print("="*30)
    print("Enter\n1:Account Information \n2:Creat Acount\n3:View Account History\n4:Deposit Money\n5:Withdraw Money\n6:exit")
    print("-" * 30)
    a=int(input("Enter your choice: "))
    if a ==1:
        Account()
    elif a==2:
        Creat_Account()
    elif a==3:
        Account_History()
    elif a==4:
        Deposit()
    elif a==5:
        Withdraw()
    elif a==6:
        break
print("Thank you for using our ATM. Goodbye!")