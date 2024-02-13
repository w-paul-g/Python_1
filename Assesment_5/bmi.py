# BMI
height = 0
while height <= 0:
    try:
        height = float(input("Enter your height(m): "))
    except ValueError:
        print("Invalid")
    if height <= 0:
        print("Invalid")
weight = 0
while weight <= 0:
    try:
        weight = float(input("Enter your weight(kg): "))
    except ValueError:
        print("Invalid")
    if weight <= 0:
        print("Invalid")

body_mass_index = weight / (height * 2)
print("Body mass index: ", body_mass_index)
print("Conclusion")
if body_mass_index < 18:
    print("Underweight")
elif 18 <= body_mass_index <= 24:
    print("Normal")
elif 25 <= body_mass_index <= 30:
    print("Overweight")
else:
    print("Abnormal Overweight")
