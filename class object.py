class Student:
    Name = 'Paul'
    Age = 18


print(Student.Name)
print(Student.Age)
print(f"Name: {Student.Name} Age: {Student.Age}")


class Employees:
    Name = 'Brian K. Maine'
    Salary = 10000000
    MaritalStatus = 'Complicated'


print(f"{Employees.Name} earns Ksh. {Employees.Salary} and his status is {Employees.MaritalStatus}")


class Parents:
    FirstName = 'John'
    LastName = 'Kimani'


parent1 = Parents()
print(parent1.FirstName)


class Parent:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName


parent1 = Parent('John', 'Kimani')
parent2 = Parent('Boniface', 'Lee')
parent3 = Parent('Lilian', 'Lou')
print(f"Parent 1: {parent1.FirstName} {parent1.LastName}")
print(f"Parent 2: {parent2.FirstName} {parent2.LastName}")
print(f"Parent 3: {parent3.FirstName} {parent3.LastName}")


class Presidents:
    def __init__(self, PrefixName, FirstName, LastName, SuffixName):
        self.PrefixName = PrefixName
        self.FirstName = FirstName
        self.LastName = LastName
        self.SuffixName = SuffixName


President1 = Presidents('H.E Hon Mzee', 'Jomo', 'Kenyatta', '')
President2 = Presidents('H.E Hon', 'Daniel Toroitich', 'Arap Moi', 'PHD')
President3 = Presidents('H.E Hon', 'Emilio', 'Mwai Kibaki', '')
President4 = Presidents('H.E Hon', 'Uhuru Muigai', 'Kenyatta', '')
President5 = Presidents('H.E Hon Dr', 'William Kipchirchir', 'Arap Samoei Ruto', 'PHD')

print(
    f"Our first president was {President1.PrefixName} {President1.FirstName} {President1.LastName} {President1.SuffixName}, followed by {President2.PrefixName} {President2.FirstName} {President2.LastName} {President2.SuffixName},then {President3.PrefixName} {President3.FirstName} {President3.LastName} {President3.SuffixName}, {President4.PrefixName} {President4.PrefixName}, {President4.FirstName} {President4.LastName} {President4.SuffixName} and the current president is {President5.PrefixName} {President5.FirstName} {President5.LastName} {President5.SuffixName}")


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")

    def display(self):
        print(f"{self.age}")


Person1 = Person('Grace', 'Kuria', 29)
print(Person1.full_name())
print(Person1.display())
