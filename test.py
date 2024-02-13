class Fruit:
    def __init__(self, Name, Colour, Price):
        self.Name = Name
        self.Colour = Colour
        self.Price = Price

    def statement(self):
        print(f"I love eating {self.Name}. The {self.Colour} variety costs Ksh.{self.Price}")


Bananas = Fruit('Bananas', 'Yellow', 5)
Avocados = Fruit('Avocados', 'Green', 15)
Strawberries = Fruit('Strawberries', 'Red', 100)
print(statement)