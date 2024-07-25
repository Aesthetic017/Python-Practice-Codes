from datetime import date
import random

class BasicAccount:
    # we will use dict data structure in-order to store the details of all account
    # it will be static
    # considering acNum as primary key i.e. var which can distinguish among all accounts uniquely
    all_accounts = {}
    # we use another static variable in-order to assign incremental account number
    new_account_number = 0

    # __init__(self, str, float)
    def __init__(self, new_name, new_balance):
        self.name = new_name
        self.acNum = BasicAccount.new_account_number + 1
        # since new account number has been assigned, so we need to increment it
        BasicAccount.new_account_number += 1
        self.balance = new_balance
        self.cardNum = ''     #initially card is not assigned
        # a tuple where the first element is an int of the month and the second element is 2-digit year
        self.cardExp = ()
        self.overdraft = False
        self.overdraftLimit = 0
        self.overdraftBalance = 0

        # Now we have to add this new account into our database which is currently a dict
        BasicAccount.all_accounts[self.acNum] = self

    # Deposits the stated amount into the account, and adjusts the balance appropriately
    def deposit(self, new_amount):
        # Deposits must be a positive amount.
        # we are checking whether it is positive or not
        if new_amount > 0:
            self.balance += new_amount
        else:
            pass

    def withdraw(self, withdraw_amount):
        # if invalid amount requested
        if withdraw_amount > self.balance:
            print("Can not withdraw £%.3f"%withdraw_amount)
        else:
            self.balance -= withdraw_amount
            print("Has withdrew £%.3f. New balance is £%.2f"%(withdraw_amount, self.balance))

    # Returns the total balance that is available in the account as a float.
    # It should also take into account any overdraft that is available
    def getAvailableBalance(self):
        # remaining overdraft amount
        remaining_overdraft_balance = self.overdraftLimit - self.overdraftBalance
        return self.balance + remaining_overdraft_balance

    # returns the balance (not taking into account the overdraft) of the account as a float.
    # If the account is overdrawn, then it should return 0.
    def getBalance(self):
        # first check whether account is overdrawn or not 
        if self.overdraftBalance > 0:
            return 0
        else:
            return self.balance

    # Should print to screen in a sensible way the balance of the account.
    # If an overdraft is available, then this should also be printed and
    # it should show how much overdraft is remaining.
    def printBalance(self):
        print("\nAmount Available in Account: £", self.balance)
        if self.overdraft and self.overdraftBalance > 0:
            print("Overdraft Remaining: £", self.overdraftLimit - self.overdraftBalance)

    # Returns the name of the account holder as a string
    def getName(self):
        return  self.name

    # Returns the account number as a string
    def getAcNum(self):
        return str(self.acNum)

    # Creates a new card number, with the expiry being 3 years to the month from now.
    # (eg: if today is 3/12/20, then the expiry date would be (12/23))
    def issueNewCard(self):
        # generating card number
        self.cardNum = str(random.randint(1000, 9999)) + \
                       str(random.randint(1000, 9999)) + \
                       str(random.randint(1000, 9999)) + \
                       str(random.randint(1000, 9999))
        today = date.today()
        # creating a new date with adding 3 more year
        exp = date(today.year + 3, today.month, today.day)
        # converting date object into tuple of int as specified in init
        self.cardExp = (int(exp.month), int(str(exp.year)[-2:]))


    # To be called before deleting of the object instance.
    # Returns any balance to the customer (via the withdraw method) and returns True.
    def closeAccount(self):
        # first check whether customer is in debt or not
        if self.overdraft and self.overdraftBalance > 0:
            print("Can not close account due to customer being overdrawn by £", self.overdraftBalance)
            return False
        else:
            # Returns any balance to the customer (via the withdraw method) and returns True
            self.withdraw(self.getBalance())
            # Clarification: You shouldnt actually delete the account instance....
            # this function will simply do the relevant house keeping in the account,
            # and return a boolean
            # this statement deletes account permanently: BasicAccount.all_accounts.pop(self.acNum)
            return True
            
    # Sets the overdraft limit to the stated amount
    def setOverdraftLimit(self, new_limit):
        self.overdraft = True
        self.overdraftLimit = new_limit

    # you must also define suitable string representations that give
    # the account name, available balance, and overdraft details
    def __str__(self):
        return "\nAccount Number   : " + str(self.acNum) + \
               "\nAc. Holder Name  : " + self.name + \
               "\nAvailable Balance: " + str(self.getAvailableBalance())+ \
               "\nOverdraft Balance: " + str(self.overdraftBalance)



# class PremiumAccount has same features as Basic
# Here I'm considering that Premium account has overdraft feature
# so we inherit all the properties of Basic and we do not require to write
# code from scratch
class PremiumAccount(BasicAccount):
    #__init__(self, str, float, float)
    def __init__(self, new_name, new_balance, overdraft_limit):
        # calling the constructor of super class BasicAccount and initializing the object
        BasicAccount.__init__(self, new_name, new_balance)
        # initializing some objects in base class itself
        # it has 1 more instance in-order to distinguish premium accounts from basic
        self.is_premium = True
        self.overdraft = True
        self.overdraftLimit = overdraft_limit

    # since overdraft is available so we change the behavior of withdraw
    # Now it will allows to withdraw amount from overdraft
    def withdraw(self, withdraw_amount):
        # find overdraft first
        remaining_overdraft = self.overdraftLimit - self.overdraftBalance

        # if invalid amount requested
        if withdraw_amount > self.balance + remaining_overdraft:
            print("Can not withdraw £%.2f"%withdraw_amount)
        else:
            # check if available balance sufficient to withdrew the amount
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
            # if account balance alone is not sufficient to give amount
            # we have to use overdraft
            else:
                amount_taken_from_b = self.balance
                self.balance = 0
                self.overdraftBalance += (withdraw_amount - amount_taken_from_b)
            print("\nHas withdrew £%.2f. New balance is £%.2f"%(withdraw_amount,
                                                                self.getAvailableBalance()))
                                                                # this is main function which is used to test the code as act as a stub
if __name__ == "__main__":
    # first test with a basic account
    ac1 = BasicAccount("John Ambrose", 1000)
    print(ac1)
    # deposit £100
    ac1.deposit(100)
    print("Available balance after deposit 100: ", ac1.getAvailableBalance())
    # withdraw 640
    ac1.withdraw(640)
    print("Available balance after deposit 100: ", ac1.getAvailableBalance())
    # try to withdrew over the limit in basic account
    ac1.withdraw(500)

    # create another basic account
    ac2 = BasicAccount("Frank Abigale", 1000)
    print(ac2)
    # lets assign this customer a card
    ac2.issueNewCard()
    print("New card Details: ", ac2.cardNum, ac2.cardExp)
    # close account
    print("is account closed: ", ac2.closeAccount())

    # printing entire account
    print("\nAll accounts are: ", BasicAccount.all_accounts.keys())

    # lets test premium accounts
    ac3 = PremiumAccount("Steve Smith", 1000, 302)
    print(ac3)
    # lets check overdraft
    ac3.withdraw(1200)
    print(ac3)
    # lets check more than total available
    ac3.withdraw(1200)
    ac4 = PremiumAccount("Abraham Benjamin", 1000, 500)
    print(ac4)
    print(PremiumAccount.all_accounts.keys())


    ac5 = BasicAccount("Frank", 340)
    print(ac5)
    print(BasicAccount.all_accounts.keys())