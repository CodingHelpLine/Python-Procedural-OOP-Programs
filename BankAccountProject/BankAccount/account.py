# import ABC and abstract method
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, accountNumber):
        '''
        Class Constructor
        :param accountNumber:  to initialize account Number
        '''
        self.__accountNumber = accountNumber
        self._balance = 0.0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, toAccount, amount):
        pass

    def getAccountNumber(self):
        return self.__accountNumber

    def getBalance(self):
        return self._balance