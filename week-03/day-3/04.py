# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student ():
    def __init__(self):
        self.summ = []
    def add_grade(self, grade):
        if grade > 0 and grade <= 5:
            (self.summ).append(grade)
    def get_average(self):
        total = 0
        for i in (self.summ):
            total += i
        average = total / len(self.summ)
        return average

student1 = Student()
student1.add_grade(5)
student1.add_grade(5)
student1.add_grade(6)
print(student1.get_average())
