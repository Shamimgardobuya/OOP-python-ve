#Create function wuthrddraw and pass in self 
#withdraw is balance remove from amount  #amount is money removed and added.
#print withdraw


class Account:
    employee="True"
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.balance=0
        self.account_number=account_number
        self.deposit=[]
        self.withdrawals=[]   
        # self.email=email
        # self.withdraw=int(withdraw)
        # self.deposit=deposit
   
    def depositing(self,amount):
        
        # self.amount=amount
        if amount<=0:
            return "amount cannot be zero"
        else:
               
               self.balance+=amount
               self.deposit.append(amount)
            #    return self.balance
               
               
           
               return f"Hello {self.account_name},your new balane is {self.balance} your deposits are {self.deposit}"
    def withdraw(self,amount):
        #    self.amount=amount
    #    z=self.balance-self.amount
       if  amount>self.balance:
           return f"Insufficient funds,your balance is {self.balance}"
       elif amount<0:
           return f"Wrong  amount "
       else:           
           self.withdrawals.append(amount)
           self.balance-=amount+100
       #    return int(self.amount)
           return f"Hello {self.account_name},your new balance is {self.balance} and your withdrawals are{self.withdrawals}"
    def deposit_statement(self):
        for x in self.deposit:
            print(f"{self.account_name} ,your deposits are {x}")
    def withdrawing_statement(self):
        for y in self.withdrawals:
         print("Hello,your withdrawals are y")
    def current(self):
        return f"Hello {self.account_name} your current balance is {self.balance}"
    
        
    