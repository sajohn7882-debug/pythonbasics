class MpesaAccount:
    def __init__(self,name,phone,balance):
        self.name=name
        self.phone=phone
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("deposit", amount)
        print(f"your balance is {self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"withdraw the {amount}")
            print(f"New balance is {self.balance}")
        else:
            print("insufficient balance")
    def check_balance(self):
        print(f"Balance is {self.balance}")

user1=MpesaAccount("Erick",254705330872,5000)
user1.check_balance()
user1.deposit(5000)
user1.check_balance()
user1=MpesaAccount("Saviour",254767839202,90000)
user1.check_balance()
user1.deposit(70000)
user1.check_balance()
user1=MpesaAccount("John",254112853053,7834)
user1.check_balance()
user1.deposit(77869)
user1.check_balance()
user1=MpesaAccount("Ian",254746378812,5670)
user1.check_balance()
user1.deposit(8975)
user1.check_balance()





