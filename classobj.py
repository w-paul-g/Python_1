# Class

class Employees:
    def __init__(self, name, gender, salary):
        # Parameters
        self.name = name
        self.gender = gender
        self.salary = salary
        self.email = name + "@gmail.com"

    # Method
    def full_name(self):
        return self.name

    def salary_increase(self):
        self.salary = float(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


class Developer(Employees):
    def __init__(self, name, gender, salary, programming_language):
        super().__init__(name, gender, salary)
        self.salary = salary
        self.programming_language = programming_language
        self.full_name = name


developer1 = Developer("Cynthia", "Female", 60000, "Python")
developer2 = Developer("Paul", "Male", 60000, "Java")

print(f"{developer1.full_name} develops using {developer1.programming_language} and earns {developer1.salary} ")

emp1 = Employees("Felix", "Male", 10000)
emp2 = Employees("Peter", "Male", 10000)
emp3 = Employees("Joseph", "Male", 10000)

print(emp1.name)
print(emp1.email)
print(f"{emp1.full_name()} is {emp1.gender} and earns Ksh.{emp1.salary}")
print(f"{emp2.full_name()} is {emp2.gender} and earns Ksh.{emp2.salary}")
print(f"{emp3.full_name()} is {emp3.gender} and earns Ksh.{emp3.salary}")
# Method
emp1.salary_increase()
emp2.salary_increase()
emp3.salary_increase()
print(emp1.salary)
print(emp2.salary)
print(emp3.salary)

Employees.raise_amount *= 3
print(emp1.raise_amount)
print(Employees.raise_amount)
emp1.salary_increase()
print(emp1.salary)

Employees.set_raise_amount(1.05)
print(Employees.raise_amount)
print(emp1.salary)


class Students:
    def __init__(self, first_name, last_name, subject1, subject2):
        self.first_name = first_name
        self.last_name = last_name
        self.subject1 = subject1
        self.subject2 = subject2
        self.full_name = f"{first_name} {last_name}"
        self.total_marks = float(subject1) + float(subject2)

    def report(self):
        print(f"{self.full_name} has achieved a total of {self.total_marks} marks.")


B1 = Students("Princess", "Lou", 92, 83)
B2 = Students("Christine", "Lou", 69, 78)
B3 = Students("Martin", "Louis", 90, 71)
B4 = Students("Boniface", "Maine", 61, 50)
B5 = Students("Chris", "Brian", 40, 21)

print(f"Name: {B1.full_name} Total Marks: {B1.total_marks}")
print(f"Name: {B2.full_name} Total Marks: {B2.total_marks}")
print(f"Name: {B3.full_name}  Total Marks: {B3.total_marks}")
print(B1.report())


class Students:
    class Undergraduate(Students):
        def __init__(self, student_id, surname, first_name, middle_name, last_name, course, year_of_enrolment):
            super().__init__(self)
            self.student_id = student_id
            self.surname = surname
            self.first_name = first_name
            self.middle_name = middle_name
            self.last_name = last_name
            self.course = course
            self.year_of_enrolment = year_of_enrolment
            self.full_name = f"{self.surname} {self.first_name} {self.middle_name} {self.last_name}"

    class PostGraduate(Students):
        def __init__(self, student_id, surname, first_name, middle_name, last_name, course, year_of_enrolment):
            super().__init__(self)
            self.student_id = student_id
            self.surname = surname
            self.first_name = first_name
            self.middle_name = middle_name
            self.last_name = last_name
            self.course = course
            self.year_of_enrolment = year_of_enrolment
            self.full_name = f"{self.surname}{self.first_name}{self.middle_name}{self.last_name}"
