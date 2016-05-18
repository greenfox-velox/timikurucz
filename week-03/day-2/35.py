# create a function that returns it's input factorial

# input = 5
# factor = 1

#WHILE:
# x = 1
# while x <= input:
#     factor *= x
#     x +=1
# print(factor)

#FOR LOOP:
# for i in range (1, input+1):
#     factor *= i
#
# print(factor)


#FUNCTION:
def factorial(number):
    factor = 1
    for i in range (1, number+1):
        factor *= i
    return (factor)
print (factorial(5))
