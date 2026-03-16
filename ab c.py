from abc import ABC, abstractmethod
# ---------------- ENCAPSULATION ----------------
class MpesaAccount:
    def __init__(salf,name,balance):
        self.name=name
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Balance: {self.__balance}")
            return True
        return False

    def get_balance(self):
        return self.__balance
    # ---------------- ABSTRACTION ----------------
class MpesaService(ABC):

    @abstractmethod
    def access_service(self, account, amount):
        pass


# ---------------- SEND MONEY ----------------
class SendMoney(MpesaService):

    def access_service(self, account, amount):
        if account.withdraw(amount):
            print(f"Sent {amount} to another user.")
        else:
            print("Transaction failed: insufficient balance.")


# ---------------- LIPA NA MPESA ----------------
class LipaNaMpesa(MpesaService):

    def access_service(self, account, amount):
        if account.withdraw(amount):
            print(f"Paid {amount} to merchant using Lipa na M-Pesa.")
        else:
            print("Payment failed: insufficient balance.")


# ---------------- FULIZA ----------------
class Fuliza(MpesaService):

    def _init_(self, limit):
        self.limit = limit

    def access_service(self, account, amount):
        balance = account.get_balance()

        if amount <= balance:
            account.withdraw(amount)
            print("Transaction completed without Fuliza.")
        elif amount <= balance + self.limit:
            overdraft = amount - balance
            account.withdraw(balance)
            print(f"Transaction completed using Fuliza overdraft: {overdraft}")
        else:
            print("Transaction exceeds Fuliza limit.")


# ---------------- M-SHWARI SAVINGS ----------------
class Mshwari(MpesaService):

    def _init_(self):
        self.savings = 0

    def access_service(self, account, amount):
        if account.withdraw(amount):
            self.savings += amount
            print(f"{amount} saved to M-Shwari. Total savings: {self.savings}")
        else:
            print("Not enough balance to save.")


# ---------------- LOANS ----------------
class Loan(MpesaService):

    def _init_(self, limit):
        self.limit = limit
        self.loan_balance = 0

    def access_service(self, account, amount):
        if amount <= self.limit:
            account.deposit(amount)
            self.loan_balance += amount
            print(f"Loan approved: {amount}. Total loan owed: {self.loan_balance}")
        else:
            print("Loan request exceeds limit.")


# ---------------- MAIN PROGRAM ----------------
account = MpesaAccount("Brian", 500)

send_money = SendMoney()
lipa = LipaNaMpesa()
fuliza = Fuliza(300)
mshwari = Mshwari()
loan = Loan(1000)

print("Initial Balance:", account.get_balance())

# Save to Mshwari
mshwari.access_service(account, 200)

# Send money
send_money.access_service(account, 100)

# Pay merchant
lipa.access_service(account, 150)

# Use Fuliza
fuliza.access_service(account, 400)

# Take loan
loan.access_service(account, 500)

print("Final Balance:", account.get_balance())
    