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
    def __eq__(self, other_entry):
        return (self.balance == other_entry.balance)
    def __str__(self):
        return 'Account({})'.format(self.balance)
    def __repr__(self):
        return 'Account({})'.format(self.balance)

    def deposit(self, ammount_to_deposit):
        self.balance = self.balance + ammount_to_deposit
    def withdraw(self, ammount_to_withdraw):
        self.balance = self.balance - ammount_to_withdraw
    def get_standing(self):
        if self.balance >= 1000:
            print ("Good")
        else:
            print ("Bad")
    def get_interest(self):
        interest = (self.balance * .05)
        return interest
        #would this variable be better if made in magic init?

# class User:
#     def __init__(self, username, uid):
#         self.username = username
#         self.uid = uid
#     def __str__(self):
#         return 'User({}, {})'.format(self.username, self.uid)
# print ("Enter account name")
# account_name = input()
# username_uid_dict = {}


print ("Enter initial deposit ammount")
initial_ammount = int(input())
#
# account_name = Account(initial_ammount)
# print (account_name.balance)
# print (account_name)

jessica = Account(2000)
justin = Account(initial_ammount)
#'business_name' = Reviews.get_avg_rating(raw_business_review_data)
#>>>'business_name' 'avg_rating'
print (justin.balance)
# b = Account.deposit(justin, 500)
# print(b)
Account.deposit(justin, 500)
print (justin.balance)
Account.withdraw(justin, 800)
print (justin.balance)
Account.get_standing(justin)
Account.get_standing(jessica)
print (Account.get_interest(justin))
print (justin.balance == jessica.balance)
print ('\n')
print (justin)
