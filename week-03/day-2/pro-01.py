# linear_search([4,5,6], 6)
# # expected output: 2
#
# linear_search([4,5,7], 6)
# # expected output: -1

def linear_search(input, number):
    index = 0
    if number in input:
        for element in input:
            if element == number:
                return index
            index += 1
    else:
        index = -1
        return index

print (linear_search([4,5,6], 6))
print (linear_search([4,5,7], -1))

#2nd version with .index():
def linear_search(input, number):
    index = 0
    if number in input :
        for element in input:
            if element == number:
                index = input.index(number)
    else:
        index = -1
    return index

print (linear_search([4,5,6], 6))
print (linear_search([4,5,7], -1))
