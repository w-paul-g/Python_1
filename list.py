#
my_list = [123, 112, 133, 4332, 543]
print(my_list)
print(my_list[1])
print(my_list[4])

#
print(my_list[0:3])

#
my_list[1] = 345
print(my_list)

#
print(len(my_list))

#
print(my_list)

#
my_list.insert(4, 456)
print(my_list)

#
my_list.extend([123, 112, 133, 4332])

#
my_list.remove(123)
print(my_list)

#
del my_list[3]
print(my_list)

#
del my_list

#
my_list2 = [134, 243, 374, 348, 4323, 2442, 323, 344, 438, 324]
print(my_list2)

#
print(min(my_list2))
print(max(my_list2))

#
print(sum(my_list2))

#
print((sum(my_list2))/(len(my_list2)))

#
print(my_list2)
if 342 in my_list2:
    print('Present')
else:
    print('Not present')


#

students = ['Brian', 'Martin', 'Chris', 'Boniface']
print(students)

if 'Brian' in students:
    print('present')
else:
    print('Not present')

students.insert(2, 'Paul')
print(students)
