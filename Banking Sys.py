from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def checkBalance(self):
        return 0


class SavingAccount(Account):
    def __init__(self):
        # [key][0] = name; [key][1] = balance
        self.accountNumber = None
        self.savingAccounts = {}

    def createAccount(self, name, initial_deposit):
        self.accountNumber = randint(10000, 99999)  # instance attribute
        self.savingAccounts[self.accountNumber] = [name, initial_deposit]
        print("Account is created :)")
        print("Account number:", self.accountNumber)

    def authenticate(self, name, account_number):
        if account_number in self.savingAccounts.keys():
            if self.savingAccounts[account_number][0] == name:
                print("Authentication Successful !")
                self.accountNumber = account_number
                return True
            else:
                print("Authentication Failed !")
                return False
        else:
            print("Authentication Failed !")
            return False

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawal_amount
            print("Withdrawal Successful !")
            self.checkBalance()

    def deposit(self, deposit_amount):
        self.savingAccounts[self.accountNumber][1] += deposit_amount
        print("Deposit Successful !")
        self.checkBalance()

    def checkBalance(self):
        print("Available Balance :", self.savingAccounts[self.accountNumber][1])


savingAccount = SavingAccount()
while True:
    print("*************************** $ Welcome to Kaiya Bank $ ***************************************** ")
    print("Enter a : Create a new saving account ")
    print("Enter b : Access existing account ")
    print("Enter c : Exit ")
    userChoice = input()
    if userChoice == 'a':
        name = input("Please Enter the Name : ")
        initialDeposit = int(input("Please enter the deposit amount:"))
        savingAccount.createAccount(name, initialDeposit)
    elif userChoice == 'b':
        name = input("Please Enter the Name : ")
        accountNumber = int(input("Enter the Account Number"))
        authenticationStatus = savingAccount.authenticate(name, accountNumber)
        if authenticationStatus:
            while True:
                print("Enter 1: Check Balance")
                print("Enter 2:  Withdrawal")
                print("Enter 3: Deposit")
                print("Enter 4: Exit")
                Ip = int(input())
                if Ip == 1:
                    savingAccount.checkBalance()
                elif Ip == 2:
                    withdrawalAmount = int(input("Please enter the withdrawal amount:"))
                    savingAccount.withdraw(withdrawalAmount)
                elif Ip == 3:
                    depositAmount = int(input("Please enter the deposit amount:"))
                    savingAccount.deposit(depositAmount)
                elif Ip == 4:
                    quit()
    elif userChoice == 'c':
        quit()

"""
Simulate a banking system
problem statement:
*Give a prompt to the user asking if the which to create a new Saving Account or access an existing one
*If the user would like to create a new account their name and initial deposit and create a 5 digit random number and
make it as account number and make it as the account number of their new saving Account
*If they are accessing an existing account,accept their name and account number to validate the user and give them
options to withdraw, deposit or display their available balance

steps :
# nouns : bank , customer  => class
#class bank -> create new account, check balance, access account,withdraw, deposit
#class customer -> give details
#we will create dic to save all details of customer
#at time of existing account we need to authenticate if user is valid
#create methods for create account,authentication,withdrawal,deposit
#any bank account should perform theses operations, so how can we make sure that none of these operations are being
missed out : we can make SavingAccount class inherit from ABC which will make use of all these methods
#abstrat class Account with help of meta class and make all methods  as abstract methods with help of decorator abstract
method , import it from module ABC
#createAccount: we need generate random 5 digit number : use randint
#map this account number to name and deposit in dictionary as key
"""
# ----------------------------------------------------------------------------------------------------------------------#
