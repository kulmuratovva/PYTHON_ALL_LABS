class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

a = float(input("Length: "))
mysquare = Square(a)
print("Square area:", mysquare.area())

myshape = Shape()
print("Shape area:", myshape.area())