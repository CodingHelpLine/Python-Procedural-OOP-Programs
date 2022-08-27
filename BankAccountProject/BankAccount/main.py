from account import Account
from checking import CheckingAccount
from savings import SavingsAccount
from bank import Bank

# Menu Function
def menu():
    choice = -1

    while choice < 0 or choice > 5:
        print("1. Create an Account")
        print('2. Check Account Balance')
        print("3. Deposit an Amount")
        print("4. Withdraw an Amount")
        print("5. Transfer an Amount")
        print('0. Exit')
        choice = int(input("Enter choice:-> "))

    return choice

# Create an account
def createAccount(bank):

    # Menu to user to select account type
    choice = -1

    while choice < 0 or choice > 2:
        print("Select Account Type")
        print("1. Checking Account")
        print("2. Savings Account")
        print("0. Back to main")
        choice = int(input("Enter choice:-> "))

    print()

    if choice == 1:
        checking = CheckingAccount(Bank.getNextAccountNumber())
        bank.addAccount(checking)
        print("Successfully created a Checking account - Account Number: ", checking.getAccountNumber())
    elif choice == 2:
        savings = SavingsAccount(Bank.getNextAccountNumber())
        bank.addAccount(savings)
        print("Successfully created a Savings account - Account Number: ", savings.getAccountNumber())


# check balance
def checkBalance(bank):
    accountNumber = int(input("Enter Account Number: "))
    bank.checkBalance(accountNumber)

# Deposit function
def doDeposit(bank):
    accountNumber = int(input("Enter Account Number: "))
    amount = float(input("Enter an Amount to deposit: "))
    bank.deposit(accountNumber, amount)

# Withdraw function
def doWithdraw(bank):
    accountNumber = int(input("Enter Account Number: "))
    amount = float(input("Enter an Amount to Withdraw: "))
    bank.withdraw(accountNumber, amount)

# Transfer function
def doTransfer(bank):
    fromAccountNumber = int(input("Enter From Account Number: "))
    toAccountNumber = int(input("Enter To Account Number: "))
    amount = float(input("Enter an Amount to Transfer: "))
    bank.transfer(fromAccountNumber, toAccountNumber, amount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    bank = Bank()

    choice = -1

    while choice != 0:
        choice = menu()
        print()

        if choice == 1: # Create account
            createAccount(bank)
        elif choice == 2: # check balance
            checkBalance(bank)
        elif choice == 3: # deposit
            doDeposit(bank)
        elif choice == 4: # withdrawal
            doWithdraw(bank)
        elif choice == 5: # transfer
            doTransfer(bank)
        else:
            print("GoodBye!...")