class Triangle:
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        # Verify if the sum of angles equals 180
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

    
    def check_triangle_type(self):
        # First, ensure the triangle is valid
        if not self.check_angles():
            return "Invalid Triangle"
        
        # Check for Obtuse (one angle > 90)
        if self.angle1 > 90 or self.angle2 > 90 or self.angle3 > 90:
            return "Obtuse Triangle"
        # Check for Acute (all angles < 90)
        elif self.angle1 < 90 and self.angle2 < 90 and self.angle3 < 90:
            return "Acute Triangle"
        # Otherwise it must be a Right Triangle
        else:
            return "Right Triangle"

class isosceles_triangle(Triangle):
    def is_isosceles(self):
        if self.check_angles():
            return (self.angle1 == self.angle2 or 
                    self.angle2 == self.angle3 or 
                    self.angle1 == self.angle3)
        return False

class right_triangle(Triangle):
    def is_right(self):
        if self.check_angles():
            return (self.angle1 == 90 or 
                    self.angle2 == 90 or 
                    self.angle3 == 90)
        return False

class equilateral_triangle(Triangle):
    def is_equilateral(self):
        if self.check_angles():
            return self.angle1 == 60 and self.angle2 == 60 and self.angle3 == 60
        return False

class isosceles_right_triangle(isosceles_triangle, right_triangle):
    def is_isosceles_right(self):
        # Checks for both properties using inherited methods
        return self.is_isosceles() and self.is_right()



# Example Usage
my_triangle = Triangle(60, 60, 60)
print(f"Is the triangle valid? {my_triangle.check_angles()}")
print(f"Triangle Type is: {my_triangle.check_triangle_type()}")
tri = isosceles_right_triangle(90, 45, 45)

print(f"Is Isosceles? {tri.is_isosceles()}")       # True
print(f"Is Right-Angled? {tri.is_right()}")       # True
print(f"Is Isosceles Right? {tri.is_isosceles_right()}") # True