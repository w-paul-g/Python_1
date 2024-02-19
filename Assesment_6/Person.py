
class Person:
    def __init__(self, surname, firstname, lastname):
        self.surname = surname
        self.firstname = firstname
        self.lastname = lastname
        self.full_name = surname + "" + firstname + " " + lastname


class Employee(Person):
    def __init__(self, surname, firstname, lastname, department, position):
        super().__init__(self, surname, firstname, lastname)
        self.department = department
        self.position = position


class Student(Person):
    def __init__(self, surname, firstname, lastname, course, year_of_enrolment):
        super().__init__(self, surname, firstname, lastname)
        self.course = course
        self.year_of_enrolment = year_of_enrolment
