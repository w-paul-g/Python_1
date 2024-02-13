#
my_tuple = (1, 2, 3, 4, 5, 22, 323, 31, 414, 44, 11, 423)
print(my_tuple)
print(my_tuple[2])
print(my_tuple[3:5])

#
print(len(my_tuple))

#
del my_tuple

#
my_tuple_2 = (1, 2, 3, 4, 5, 22, 323, 31, 312, 323)

#
print(my_tuple_2.count(323))

#
print(max(my_tuple_2))
print(min(my_tuple_2))

#
print(sum(my_tuple_2))

#
print(sum(my_tuple_2) / len(my_tuple_2))

#
print(my_tuple_2.index(312))
print(my_tuple_2.index(323))

#
if 234 in my_tuple_2:
    print('present')
else:
    print('not present')




