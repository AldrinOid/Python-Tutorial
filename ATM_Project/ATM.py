import time
import msvcrt
from datetime import datetime
import os

user_pin = "1234"
user_balance = 100000

# Function to show the ATM menu
def showMenu():
    print("=====Welcome to the ATM=====")
    print("|1. Check Balance          |")
    print("|2. Deposit Money          |")
    print("|3. Withdraw Money         |")
    print("|4. Exit                   |")
    print("============================")


# Function to check the user balance
def checkBalance():
    print(f"Your current balance is ${(user_balance)}")
    print('\n')
    choose_receipt = input("Do you want to print your receipt? (yes/no): ").strip().lower()
    if choose_receipt == "yes":
        os.system('cls')
        print("Printing receipt...")
        time.sleep(1)
        os.system('cls')
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"--- ATM Receipt ---\nDate & Time: {date_time}\nBalance: ${user_balance}\nThank you for using our ATM!\n")
        
        time.sleep(2)
        
    else:
        os.system('cls')
        print("No receipt printed.")
    
    goBackToMenu()

# Function to deposit money into the user's account
def depositMoney():
    global user_balance
    try:
        deposit_amount = float(input("Enter the amount to deposit: $"))
        if deposit_amount <= 0:
            print("Please enter a valid amount greater than zero.")
            return
        user_balance += deposit_amount
        print(f"Successfully deposited ${deposit_amount}. Your new balance is ${user_balance}.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

    goBackToMenu()


# Function to withdraw money from the user's account
def withdrawMoney():
    global user_balance
    try:
        withdraw_amount = float(input("Enter the amount to withdraw: $"))
        if withdraw_amount <= 0:
            print("Please enter a valid amount greater than zero.")
            return
        elif withdraw_amount > user_balance:
            print("Insufficient funds. Please enter a smaller amount.")
            return
        user_balance -= withdraw_amount
        print(f"Successfully withdrew ${withdraw_amount}. Your new balance is ${user_balance}.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

    goBackToMenu()


# Function to go back to the main menu
def goBackToMenu():
    choose_yes_no = input("Do you want to go back to the main menu? (yes/no): ").strip().lower()
    if choose_yes_no == "yes":
        print("Going back to the main menu...")
        time.sleep(2)
        os.system('cls')
        goBackToMenu()
    else:
        quitATM()


# Function to quit the ATM
def quitATM():
    print("Exiting the ATM.")
    time.sleep(2)
    print("Thank you for using our service!")


# Function to handle user login
def login():
    attempts = 0
    while attempts < 3:
        welcomeMessage()
        os.system('cls')
        pin = input("Please enter your PIN: ")
        if pin == user_pin:
            print("Login successful!")
            os.system('cls')
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. You have {3 - attempts} attempts left.")
    print("Too many incorrect attempts. Exiting the ATM.")
    return False


# Function to display a welcome message
def welcomeMessage():
    print("Welcome to the ATM! Please log in to continue.")
    print("Press any key to continue...")
    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            break


# Main function to run the ATM program
def main():
    if login():
        showMenu()
        while True:
            choice = input("Please choose an option (1-4): ")
            if choice == "1":
                os.system('cls')
                checkBalance()
            elif choice == "2":
                os.system('cls')
                depositMoney()
            elif choice == "3":
                os.system('cls')
                withdrawMoney()
            elif choice == "4":
                quitATM()
                break
            else:
                print("Invalid choice. Please try again.")

main()


