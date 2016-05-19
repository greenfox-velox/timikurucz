# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle ():
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        circumference = 2 * self.radius * 3.14
        return circumference
    def get_area(self):
        area = self.radius**2 * 3.14
        return area


kor = Circle(5)
print (kor.get_circumference())
print (kor.get_area())
