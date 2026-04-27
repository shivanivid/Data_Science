class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

# Example of creating an instance
test_triangle = Triangle(60, 60, 60)

print(f"Angles: {test_triangle.angle1}, {test_triangle.angle2}, {test_triangle.angle3}")