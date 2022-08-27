# import Acccount class
from account import  Account

class CheckingAccount(Account):

    # provide constructor
    def __init__(self, accountNumber):
        super().__init__(accountNumber)
        self.__fee = 1.75

    # override abstract functions

    # Deposit
    def deposit(self, amount):

        # must be positive value
        if amount > 0:
            self._balance += amount
            self._balance -= self.__fee
            return True
        else:
            print("ERROR: Deposit amount must be positive")
            return False

    # Withdrawal Function
    def withdraw(self, amount):

        # positive value
        if amount > 0:
            # Sufficient balance
            if (self._balance + self.__fee) >= amount:
                self._balance -= amount
                self._balance -= self.__fee
                return True

            else:
                print("ERROR: Insufficient Balance to withdraw", amount)
        else:
            print("ERROR: Withdrawal amount must be positive.")

        return False
    # Transfer Functions
    def transfer(self, toAccount, amount):

        # check amount positive
        if amount > 0:
            # Check balance
            if self._balance >= amount:
                toAccount.deposit(amount)
                self._balance -= amount
                return True
        else:
            print("ERROR: Transfer amount should be positive")

        return False