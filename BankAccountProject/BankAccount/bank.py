# import account
from account import Account

class Bank(object):
    nextAccountNumber = 1000

    def __init__(self):
        self.__accounts = []

    def addAccount(self, account):
        self.__accounts.append(account)

    def findAccount(self, accountNumber):

        for account in self.__accounts:
            if account.getAccountNumber() == accountNumber:
                return account

        return None

    def deposit(self, accountNumber, amount):
        account = self.findAccount(accountNumber)

        if account != None:
            if account.deposit(amount):
                print("Success: Transaction completed")
            else:
                print("ERROR: Transaction Failed")
        else:
            print("ERROR: No such account exist with Account Number", accountNumber)

    def withdraw(self, accountNumber, amount):
        account = self.findAccount(accountNumber)

        if account != None:
            if account.withdraw(amount):
                print("Success: Transaction completed")
            else:
                print("ERROR: Transaction Failed")
        else:
            print("ERROR: No such account exist with Account Number", accountNumber)

    def transfer(self, fromAccountNumber, toAccountNumber, amount):
        fromAccount = self.findAccount(fromAccountNumber)
        toAccount = self.findAccount(toAccountNumber)

        if fromAccount != None and toAccount != None:
            if fromAccount.transfer(toAccount, amount):
                print("Success: Transaction is successful!")
            else:
                print("ERROR: Transaction Failed")
        else:
            print("ERROR: One of the To or From account doesn't exist")
        return False

    def checkBalance(self, accountNumber):
        account = self.findAccount(accountNumber)

        if account != None:
            print("Balance is:", account.getBalance());
        else:
            print("ERROR: No such account exist with account number:", accountNumber)

    @classmethod
    def getNextAccountNumber(cls):
        cls.nextAccountNumber += 1
        return cls.nextAccountNumber