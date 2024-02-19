class Staff:
    def __init__(self, surname, first_name, last_name):
        self.surname = surname
        self.first_name = first_name
        self.last_name = last_name


class Teacher(Staff):
    def __init__(self, surname, first_name, last_name, tsc_no, subjects, other_roles):
        super().__init__(self, surname, first_name, last_name)
        self.tsc_no = tsc_no
        self.subjects = subjects
        self.other_roles = other_roles


t1 = Teacher("John", "Doe", "Harry", "Smith", "Mathematics", "")
