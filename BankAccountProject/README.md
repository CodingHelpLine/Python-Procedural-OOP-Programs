# Bank Account Application

Application to demonstrate Object Oriented programming concepts of Python Programming
language including Inheritance, Abstract Classes using ABC @abstractmethod annotation or
decorator, Overriding, Polymorphism with User Interactive Menu driven application for the
sake of learning programming. It also includes aggregation relationship represented by Bank
class to manage the bank acounts.

## Is-a Relationship

* Is-a relationship indicates that A class Is a subclass of another class. Is-a relationship promotes code reuse which is the basic advantage of Object Oriented Programming. For example A Person is a base class, and A Student is a subclass. Now the student is a Person also.
* Polymorphism provides another advantage where child classes can override the base class methods and provide their own functionality.
* Abstract classes cannot be instantiated.
* Pure Virtual methods must be overridden in child classes.
* We create objects on the heap to use polymorphism.

## Classes

* BankAccount abstract class – Fields balance, account number
* CheckingAccount class – Subclass of Account class. Transaction fee
* SavingsAccount class – subclass of Account class. Yearly Interest Rate for profit.
* Bank class - Manages the Accounts
* Driver code – Provides Menu driven User Interaction. User can select an account, deposit, withdraw Funds. Apply interest rate on Savings account.
