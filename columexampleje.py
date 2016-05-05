#this doesn't work

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, False]

interleaved = list(zip(list1, list2, list3))
uninterleaeved = list(zip(*interleaved)

print (interleaved)

print (uninterleaved)
