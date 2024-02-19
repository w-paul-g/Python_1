class Calculator:
    def __init__(self, num1, num2, num3, num4, num5, num6,):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6

    @self.addition
    def addition(self, num1, num2, num3, num4, num5, num6):
        sum = num1 + num2 + num3 + num4 + num5 + num6
        value = sum

    @self.subtraction
    def subtraction(self, num1, num2, num3, num4, num5, num6):
        diff = num1 - num2 - num3 - num4 - num5 - num6
        value = diff

    @self.multiplication
    def multiplication(self, num1, num2, num3, num4, num5, num6):
        product = num1 * num2 * num3 * num4 * num5 * num6
        value = product

    @division
    def division(self, num1, num2, num3, num4, num5, num6):
        divisor = num1 / num2 / num3 / num4 / num5 / num6
        value = divisor

    def display(self):
        print(value)

n1 =Calculator(int(input("Enter first number: ")),int(input("Enter second")))