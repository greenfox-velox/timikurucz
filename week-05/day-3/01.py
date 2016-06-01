# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def division(number):
    try:
        print(10 / number)
    except ZeroDivisionError:
        print('Fail')

division(10)
division(0)
