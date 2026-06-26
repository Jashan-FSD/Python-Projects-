# Function for PIN Login & Security Checking
def login():

    login_count = 5

    while login_count <= 5:

        if login_count == 0:
            print("You cannot login right now try again later!")
            return False

        pin = 1234
        user_pin = int(input("Enter your ATM PIN: "))

        if user_pin == pin:
            print("Login Successful!\n")
            return True
        else:
            login_count -= 1
            print("Invalid PIN!, Remaining chances left are " + str(login_count) )

# Function to check balance
def check_balance(balance):
    print("Current Balance = ₹", balance)

# Function to deposit money
def deposit(balance):
    amount = float(input("Enter amount to deposit: ₹"))
    balance = balance + amount
    print("Deposit Successful!")
    print("Updated Balance = ₹", balance)
    return balance

# Function to withdraw money
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful!")
    else:
        print("Insufficient Balance!")

    print("Current Balance = ₹", balance)
    return balance

# Main Program
balance = 5000

if login():

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance(balance)

        elif choice == 2:
            balance = deposit(balance)

        elif choice == 3:
            balance = withdraw(balance)

        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid Choice!")