# Conditional Statement

# Iteration Statement

# if...else
age = 23
if age >= 18:
    print("You are old enough to move out")
    print("You are expected to have an ID")
else:
    print("You are not old enough to move out")

# if...elif..else
grade = 89
if 80 <= grade <= 100:
    print("You are an A material")
elif 70 <= grade <= 80:
    print("You are a B material")
elif 50 <= grade <= 70:
    print("You are a C material")
elif 40 <= grade <= 50:
    print("You are a D material")
elif 20 <= grade <= 40:
    print("You are a E material")
elif 0 <= grade <= 20:
    print("You are a F material")
else:
    print("We don't have your marks recorded")


# Exercise

Temperature = float(input("Temperature: "))
if Temperature < 20:
    print("Put on a Sweater.")
elif Temperature < 30:
    print("Put on a shirt and take off your sweater.")
else:
    print("Take off your shirt.")
