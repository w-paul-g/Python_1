# Dictionary

# 1
my_dictionary = {
    "Name": "Paul",
    "Gender": "Male",
    "Status": "Single"

}
print(my_dictionary)

# 2
my_dictionary = dict(
    Name="Paul",
    Gender="Male",
    Status="Single"
)
print(my_dictionary)

# Print specific values in an element
print(my_dictionary['Gender'])
print(my_dictionary.get('Status'))
print(my_dictionary.get('Name'))
print(my_dictionary['Name'])

# Edit a specific value element
my_dictionary['Status'] = "Complicated"
print(my_dictionary)

# Adding a key value elements
my_dictionary['BirthDate'] = '31/01/2006'
print(my_dictionary)
my_dictionary['Residence'] = 'Nakuru'
print(my_dictionary)
my_dictionary['Email'] = 'w.paul.g@proton.me'
print(my_dictionary)

# Copying from one dictionary to another
my_dictionary_2 = my_dictionary.copy()
print(my_dictionary_2)

# Dictionary Length
# Number of elements in a dictionary
print(len(my_dictionary))

# Remove element

# obj__.pop
my_dictionary.pop('Status')
print(my_dictionary)
print(my_dictionary_2)

# del obj__[el__]
del my_dictionary_2['Email']
print(my_dictionary_2)
print(my_dictionary)

# Clear Dictionary

# obj__clear()
my_dictionary.clear()
print(my_dictionary)
print(my_dictionary_2)

# del obj__
del my_dictionary
print(my_dictionary_2)

#
if 'Name' in my_dictionary_2:
    print('Name found')
else:
    print('Name not found')

# Print Dict Values
for value in my_dictionary_2:
    print(my_dictionary_2[value])

#
for key in my_dictionary_2:
    print(key)

#
for key, value in my_dictionary_2.items():
    print(key, value)


#
shop1 = {
    'Maize Flour': 100,
    'Wheat Flour': 200,
    'Millet Flour': 210,

}
print(shop1)

if 'Maize Flour' in shop1:
    print('There is Maize Flour')
else:
    print('There is No Maize Flour')

shop1['Meat'] = '1000'
print(shop1)


