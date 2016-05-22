# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has


def make_tree(input):
    length_row = input - 1
    star_numbers = 1
    for i in range (input):
        print((' ' * length_row), ('*' * (star_numbers)))
        star_numbers += 2
        length_row -= 1

make_tree(8)
