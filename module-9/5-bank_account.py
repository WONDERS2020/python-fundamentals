#/usr/bin/python3
""" A module that create a bank account class with private attribute"""

class BankAccount:
    """ A class representing a bank account."""

    def __init__(self, initail_balance=0):
        """Initialize tha bank account with an optional initial balance."""
        self.__balance = initail_balance

    def deposit(self, amount):
        """ Deposit money into the account."""
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        """ Get the current blance of the amount."""
        return self.__balance
    def withdraw(self, amount):
        pass
if __name__ == '__main__':

        h_account = BankAccount(5000)

        h_account.deposit(100)
        print("Current balance:", h_account.get_balance())

        h_account._balance = 1000
        print("Attemting to change balance directly:", h_account.get_balance())