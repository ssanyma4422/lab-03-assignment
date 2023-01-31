class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle("red", 10, 20)
print("Rectangle area:", rect.area(), " color:", rect.color)

circle = Circle("blue", 5)
print("Circle area:", circle.area(), " color:", circle.color)
