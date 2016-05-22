# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def make_diamond(input):
    length_row = input
    star_numbers = 1
    for i in range (input):
        print((' ' * length_row), ('*' * (star_numbers)))
        star_numbers += 2
        length_row -= 1
    for i in range (input, -1, -1):
        print((' ' * length_row), ('*' * (star_numbers)))
        star_numbers -= 2
        length_row += 1
make_diamond(11)
