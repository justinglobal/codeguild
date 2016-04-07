


class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    # def setup(self, name, phone_number):
    #     self.name = name
    #     self.phone_number = phone_number
    def area_code(self):
        return self.phone_number.split('-')[0]
    def __eq__(self, other_entry):
        return (self.name == other_entry.name
        and self.phone_number == other_entry.phone_number)
    def __str__(self):
        return 'AddressBookEntry({}, {})'.format(self.name,self.phone_number)

# me = AddressBookEntry()
# AddressBookEntry.setup(me, 'David', '503-555-9895')
#
# print (AddressBookEntry.area_code(me))  #> '503'

# entry = AddressBookEntry()
# entry.setup('Justin', '503-974-4597')

entry = AddressBookEntry('Justin' , '503-974-4597')
entry2 = AddressBookEntry('Jolene' , '503-555-9999')

print (entry.area_code())  #> '503'
print (entry.name)
print (entry.phone_number)

print (entry2.area_code())  #> '503'
print (entry2.name , entry2.phone_number)
print (entry2.phone_number)

print (entry == entry2)
print (AddressBookEntry.__eq__(entry, entry2))
print (entry2)
x = 3
x
print (x)
