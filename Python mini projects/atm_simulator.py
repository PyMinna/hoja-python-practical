balance = 5000

def show_menu():
    print("===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    print("Current Balance: ₹", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    
    if amount > 0:
        balance += amount
        print("₹", amount, "deposited successfully")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= balance:
        balance -= amount
        print("₹", amount, "withdrawn successfully")
    else:
        print("Insufficient balance")

while True:
    show_menu()
    
    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice! Try again")