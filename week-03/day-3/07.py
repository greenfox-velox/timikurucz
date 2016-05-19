# create a function that takes a list and returns a new list with all the elements doubled

my_list = [1, 2, 3]

def double_list (input):
    new_list = input * 2
    return new_list
print (double_list(my_list))


def doubled_elements (input):
    doubled_list = []
    for i in range(len(input)):
        doubled_list += [input[i] * 2]
    return uj
print (doubled_elements(my_list))
