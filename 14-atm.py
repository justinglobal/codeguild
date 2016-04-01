# Practice: ATM
# Write a program that functions as a simple ATM for a single account.
#
# An account will be a class: it will have a field for the balance.
#
# Write functions for the account class that:
#
# -Deposit to the account.
# -Check if enough funds for a withdrawal.
# -Withdraw an allowed amount.
# -Calculate 0.5% interest on the account.
# -Implement a user interface that lets a user pick each of those actions
#     and updates the account. After each action it will print the balance.
#
# Advanced
#
# Save the account balance to a file after each operation. Read that balance on startup so the balance persists across program starts.
# Add to each account class an account ID number.
# Allow the user to open more than one account. Let them perform all of the above operations by account number.

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, ammount_to_deposit):

        self.balance = self.balance + ammount_to_deposit

    def withdraw(self, ammount_to_withdraw):
        self.balance = self.balance - ammount_to_withdraw

    def get_standing(self):
        if self.balance >= 1000:
            print ("Good")
        else:
            print ("Bad")
        # return self.balance >= 1000

print ("Enter account name")
account_name = input()

print ("Enter initial deposit ammount")
initial_ammount = int(input())

account_name = Account(initial_ammount)
print (account_name.balance)

jessica = Account(2000)
justin = Account(1000)
print (justin.balance)
# b = Account.deposit(justin, 500)
# print(b)
Account.deposit(justin, 500)
print (justin.balance)
Account.withdraw(justin, 800)
print (justin.balance)
Account.get_standing(justin)
Account.get_standing(jessica)
