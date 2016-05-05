print_this = [['the', 875], ['of', 627], ['in', 278], ['and', 270], ['a', 270], ['to', 248], ['that', 132], ['or', 131], ['with', 126], ['is', 110]]
##>>> print_this
[['the', 875], ['of', 627], ['in', 278], ['and', 270], ['a', 270], ['to', 248], ['that', 132], ['or', 131], ['with', 126], ['is', 110]]
##>>> print(print_this)
[['the', 875], ['of', 627], ['in', 278], ['and', 270], ['a', 270], ['to', 248], ['that', 132], ['or', 131], ['with', 126], ['is', 110]]
print_list = print_this
##>>> print_list
[['the', 875], ['of', 627], ['in', 278], ['and', 270], ['a', 270], ['to', 248], ['that', 132], ['or', 131], ['with', 126], ['is', 110]]



for item in (print_list):
  print (item[0], ', '.join(map(str, item[1:])))

#the code above returns the data in the list in the format below

##the 875
##of 627
##in 278
##and 270
##a 270
##to 248
##that 132
##or 131
##with 126
##is 110

x = 3
x
print (x)
