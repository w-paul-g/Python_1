print("Hello World!")
print('Welcome to eMobilis Institution')
print(800)

# variables
age = 18
age1 = 23
print(age)
first_name = 'Paul'
print(first_name)
lastname = 'Gichuki'
print(lastname)
full_name = first_name + ' ' + lastname
print(full_name)

# data types

# string
print("String")
school = "eMobilis"
print(school)

# integer
print(123)
num_1 = 154
print(num_1)

# float
print(10.2498958)
num_2 = 15.877827837
print(num_2)

# boolean
is_true = False
is_false = True

# list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Paul', "Felix", "Esther", "Faith"]
print(my_list)
print(my_list[10])

# set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'Mwanza'}
print(my_set)

# dictionary
my_dictionary = {"Name": "Paul", "Age": 18, "Gender": "Male"}
print(my_dictionary["Name"])
print(my_dictionary["Gender"])
print(my_dictionary["Age"])
my_dictionary["School"] = "eMobilis"
print(my_dictionary)
my_dictionary["Age"] = 19
print(my_dictionary)

#  tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, "Alpine")
print(my_tuple[0:9])
print(my_tuple)

# input
FirstName = input("Enter your first name: ")
LastName = input("Enter your last name: ")
# Age = input("What is your age? ")
BirthYear = input("What is your birth year? ")
AgeN = 2024 - int(BirthYear)
print(AgeN)
Location = input("What is your location? ")
print("Hello" + " " + FirstName + ", Welcome to eMobilis Institution")

# Area
Length = input("Length: ")
Width = input("Width: ")
Area = float(Length) * float(Width)
print(Area)
# Volume
Height = input("Height: ")
Volume = float(Area) * float(Height)
print("Volume=" + str(Volume))

# sum graduate
Age = input("Age: ")
Age_of_Graduation = (int(Age) + 4)
print(Age_of_Graduation)

#sum
First = input("Number 1? ")
Second = input("Number 2? ")
Sum = float(First) + float(Second)
print("Sum=" + str(Sum))
