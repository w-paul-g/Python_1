# Arithmetic Operator
# +, -, *, %, **

# Example
a = 5
b = 4

# Addition
print(a + b)

# subtraction
print(a - b)

# Multiplication
print(a * b)

# Division
print(a / b)

# Percentage
print(a % b)

# Powers
print(a ** b)

# Assignment Operator

# Addition
c = 10
c = c + 5
print(c)

c += 5
print(c)

# Subtraction
d = 7
d = d - 4
print(d)

d -= 4
print(d)

# Multiplication
e = 8
e = e * 2
print(c)

e *= 2
print(c)

# Division
f = 4
f = f / 2
print(f)

f /= 2
print(f)

# Comparison Operator
# ==, !=, <=, >=, <, >

# Example
e = 10
f = 20

# Equal To
print(e == f)

# Negation / Not Equal To
print(e != f)

# Less Than
print(e < f)

# Greater Than
print(e > f)

# Less Than or Equal To
print(e <= f)

# Greater Than or Equal To
print(e >= f)

# Logical Operators
# and, or, not

# Example
d = 9
f = 16

# And
print((d < f) and (d > f))
print((d < f) and (d > f))
print((d > f) and (d == f))
print((d < f) and (d == f))

# Or
print((d > f) or (d < f))
print((d < f) or (d > f))
print((d > f) or (d == f))
print((d < f) or (d == f))

# Not
print(not ((d > f) and (d < f)))
print(not ((d > f) or (d < f)))

# Identity Operator
# is, is not

# Examples
x = 6
y = 3

# is
print(x is y)

# is not
print(x is not y)

# is type
print(x is type(y))
print(type(x) is type(y))

# Membership Operator

# Example
a = 'Welcome to Full Stack Software Development'

# in
print('welcome' in a)
print('Welcome' in a)
print('stack' in a)
print('Stack' in a)

# not in
print('full' not in a)
print('welcome' not in a)
print('Welcome' not in a)
print('stack' not in a)
print('Stack' not in a)

# Exercise

input("x=")
input("y=")
print(int(x or y))
