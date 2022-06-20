
from curses import ALL_MOUSE_EVENTS
from datetime import datetime
from optparse import AmbiguousOptionError
from unicodedata import name
class Account:
    employee="True"
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.balance=0
        self.account_number=account_number
        self.deposit=[]
        self.withdrawals=[] 
        self.loan_balance=0
        # self.deposit_list=[]
        self.depo_counter=0
        # self.withdraw_list=[]

   
    def depositing(self,amount):
        
        # self.amount=amount
        if amount<=0:
            return "amount cannot be zero"
        else:
               
               self.balance+=amount
               z=datetime.now()
               self.deposit.append({"date":z.strftime('%d/%m,%y, %H:%M:%S'),"amount":amount,"narration":"deposit"})
         
               self.depo_counter+=1
               return f"Hello {self.account_name},your new balane is {self.balance} you deposited {amount} on {z.strftime('%d/%m,%y, %H:%M:%S')}"
    def withdraw(self,amount):
  
        
       if  amount>self.balance:
           return f"Insufficient funds,your balance is {self.balance}"
       elif amount<0:
           return f"Wrong  amount "
       else:           
           self.balance-=amount+100
           p=datetime.now() #fee still counted 
           self.withdrawals.append({"date":p.strftime('%d/%m/%y, %H:%M:%S'),"amount":amount,"narration":"withdraw"})

           return f"Hello {self.account_name},your new balance is {self.balance} and you have withdrawn {amount} {p.strftime('%d/%H:%M:%S')}" 

    def deposit_statement(self):
        for x in self.deposit:
            print(f"{self.account_name} ,your deposits are {x}")
        for y in self.withdrawals:
         print("Hello,your withdrawals are y")
    def current(self):
        return f"Hello {self.account_name} your current balance is {self.balance}"
    def full_statement(self):
        n=list(self.deposit)
        withdraw1=list(self.withdrawals)
        for i in n:
            print(f"{n[0]['date'],n[0]['narration'],n[0]['amount']}")
        for i in withdraw1:
            print(f"{withdraw1[0]['date'],withdraw1[0]['narration'],withdraw1[0]['amount']}")
    
        
   
    def borrow(self,amount):

        self.loan_balance=0
        # for k,v  in self.deposit:
            # if "amount" in k:
        for item in self.deposit:

            
                sum=0
                sum+=item["amount"]
                b=1//3*sum
                if amount<=b and self.depo_counter==10 and self.balance==0:
                     self.loan_balance=+amount
                     interest=0.03*self.loan_balance
                     final=interest+self.loan_balance
                     print(f"You have received a loan of {self.loan_balance} on ,you will be charged an interest of {interest}")
                else:
                    print("Dear customer,you are not legible for a loan")
    def loan_repayment(self,amount):
        self.loan_balance-=amount
        self.balance+=self.loan_balance
        print(f"Your debt is fully paid, your account is {self.balance}")
    def money_transfer(self,name,account2):
        self.name=name
        if amount<self.balance:
            self.balance-=amount   #amount belonging to first user.
            




   
#  Add a new method transfer which accepts two attributes
#   (amount and instance of another account). If the amount is less than the current
#    instances balance, the method transfers the requested amount from the current account 
#    to the passed account. The transfer is accomplished by reducing the current account balance and 
#    depositing the requested amount to the passed account.
#create money transfer function
#put in self,amount , and another account3 /class Account
#create object account and the amount needed
#create condition if the amount is more,then print less money
#if less,remove from current balance of first account and add to second account.
    # def money_transfer(self,amount,class Account)    $#using

   
                    




# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance    #function can have amount as parameter
# Overpayment of a loan increases a customers current deposit        #loan-=amount+interest
                                                                      #overpayment=balance 
                                                                      #add to deposit list.


        
