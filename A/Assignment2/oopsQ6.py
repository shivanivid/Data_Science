from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method will be implemented by subclasses"""
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

sq_area = Square(5)
circle_area = Circle(3)

print(f"Square Area: {sq_area.area()}")
print(f"Circle Area: {circle_area.area()}")