# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

# input = 6
# star_numbers = 1
# for i in range (input):
#     print ('*' * star_numbers)
#     star_numbers += 1

def make_triangle(input):
    star_numbers = 1
    for i in range (input):
        print ('*' * star_numbers)
        star_numbers += 1

make_triangle(6)
