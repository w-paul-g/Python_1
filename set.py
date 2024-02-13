#
my_set = {1, 2, 3, 4, 5}
print(my_set)

#
var1 = 2
if var1 in my_set:
    print(var1)


#
my_set.add(9)
print(my_set)

#
my_set.update([4, 7, 8, 9, 45])
print(my_set)

#
my_set2 = my_set.copy()
print(my_set2)

#
print(max(my_set))
print(min(my_set))

#
print(sum(my_set))

#
my_set.discard(2)
print(my_set)

#
my_set.clear()
del my_set

#
if 32 in my_set2:
    print(32 in my_set2)
else:
    print("Not found")





