# Functions
# print("Hello World")
# print("Hello World")
# print("Hello World")

def hello_world():
    print("Hello World")
    print("Hello World")
    print("Hello World")


hello_world()


def nyumba(name):
    print(name)
    print(name)
    print(name)


nyumba("Paul")
nyumba("Mwanza")
nyumba("Felix")
nyumba("Elvis")


def num(nambari):
    print(nambari)
    print(nambari)
    print(nambari)


num(56)


def num1(fname):
    print(fname + " is my favorite person")


num1("Paul")


def students(first_name, last_name, ):
    print(first_name + " " + last_name + " please enter your name")


students("Paul", "Gichuki")


def employees(first_name, age):
    if age < 20:
        print(first_name + ", you are below 20 years old.")
    elif age <= 30:
        print(first_name + ", you are middle aged.")
    else:
        print(first_name + ", you are older than 30 years old.")


employees("Paul", 18)
employees("Gichuki", 10)


def age_calculator(age):
    new_age = age + 10
    return new_age


calculated_age = age_calculator(20)
print(calculated_age)
print(age_calculator(17))
print(age_calculator(25))


def performance_calculator(*subjects):
    total = sum(subjects)
    return total


perf = performance_calculator(45, 34)
print(perf)
student2 = performance_calculator(39, 91)
print(student2)
student3 = performance_calculator(68, 87, 67)
print(student3)


def cost(*purchase):
    total = sum(purchase)
    return total


purchase1 = cost(1, 200)
print(cost(1, 200))


def ongeza(x):
    return x * x


ongeza = ongeza(5)
print(ongeza)
