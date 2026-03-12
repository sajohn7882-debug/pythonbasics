# Simple M-Pesa System Simulation

balance = 1000  # starting balance

def check_balance():
    print("Your balance is:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposit successful.")
    print("New balance:", balance)

def send_money(amount, phone):
    global balance
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Sent KES {amount} to {phone} successfully.")
        print("Remaining balance:", balance)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", balance)


while True:
    print("\n--- M-Pesa Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Send Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Select option: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "3":
        phone = input("Enter recipient phone number: ")
        amount = float(input("Enter amount to send: "))
        send_money(amount, phone)

    elif choice == "4":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "5":
        print("Thank you for using M-Pesa.")
        break

    else:
        print("Invalid option. Try again.")