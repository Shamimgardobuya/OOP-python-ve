#Create function wuthrddraw and pass in self 
#withdraw is balance remove from amount  #amount is money removed and added.
#print withdraw


class Account:
    employee="True"
    def __init__(self,account_name,account_number,balance,email,withdraw):
        self.account_name=account_name
        self.balance=balance
        self.account_number=account_number
        self.email=email
        self.withdraw=int(withdraw)
        # self.deposit=deposit
    def withdrawal(self,amount):
       self.amount=amount
       self.withdraw-=self.balance
       return int(self.amount)
       return f"Hello {self.account_name},the balance is {self.balance}"
    def depositing(self,amount):
        self.amount=amount
        self.balance+=amount
        return self.balance
        return f"Hello {self.account_name} , you have deposited{self.balance}"
        
        
    