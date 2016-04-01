


class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    # def setup(self, name, phone_number):
    #     self.name = name
    #     self.phone_number = phone_number
    def area_code(self):
        return self.phone_number.split('-')[0]

# me = AddressBookEntry()
# AddressBookEntry.setup(me, 'David', '503-555-9895')
#
# print (AddressBookEntry.area_code(me))  #> '503'

# entry = AddressBookEntry()
# entry.setup('Justin', '503-974-4597')

entry = AddressBookEntry('Justin' , '503-974-4597')

print (entry.area_code())  #> '503'
print (entry.name)
print (entry.phone_number)
