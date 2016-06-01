# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016
class Person:
    def __init__(self,  name, birth_date):
        self.name = name
        self.birth_date = birth_date
        if birth_date < 0 or birth_date > 2016:
            raise ValueError()

student1 = Person('Bela', 1987)
student1 = Person('Belus', 2020)



# class Person:
#     def __init__(self,  name, birth_date):
#         self.name = name
#         self.birth_date = birth_date
#         if birth_date < 0 or birth_date > 2016:
#             raise ValueError("It's not a valid date")
# try:
# student1 = Person('Bela', 1987)
# student1 = Person('Belus', 2020)
# except valueError as e:
#     print(e)
