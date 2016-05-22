# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person:
    def __init__(self,  first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print ('Hi I am ' + self.first_name + ' ' + self.last_name)

class Student (Person):
    def __init__(self, first_name, last_name):
        super() .__init__(first_name, last_name)
        #innentol lehet hivatkozni a personre, amit orokol
        self.grades = []

    def add_grade (self, new_grade):
        self.grades.append(new_grade)

    def salute (self):
        self.greet()
        summa = 0
        for grade in self.grades:
            summa += grade
        print(summa / len(self.grades))



belus = Student('Bela', 'Kiss')
belus.add_grade(1)
belus.add_grade(3)
belus.salute()
